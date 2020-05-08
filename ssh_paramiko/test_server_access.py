import time

import paramiko
import requests

from contextlib import contextmanager

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


host = "192.168.56.101"
user = "user"
secret = "admin"
port = 22


def get_request_status(hostname: str) -> int:
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=3)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    return session.get(f"http://{hostname}/opencart/").status_code


class SSHClint:
    def __enter__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=host, username=user, password=secret, port=port)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


@contextmanager
def get_ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=secret, port=port)
        yield client
    except ConnectionError:
        print("Connection error!")
    finally:
        client.close()


def wait_for_ok_status_opencart(timeout: int):
    t = 0
    while t <= timeout:
        if get_request_status(host) == 200:
            print(f"Finished in {t} secs")
            break
        else:
            time.sleep(1)
            t += 1
        if t == 30:
            raise AssertionError(f"Сервис недоступен, timeout={timeout}")


def test_reboot_and_check():
    if get_request_status(host) == 200:
        with get_ssh_client() as client:
            client.exec_command('sudo reboot')
            wait_for_ok_status_opencart(30)
    else:
        raise ConnectionError("Сервис недоступен, невозможно произвести перезагрузку.")


def test_reboot_services_and_check():
    if get_request_status(host) == 200:
        with get_ssh_client() as client:
            client.exec_command('sudo systemctl restart mysql.service')
            client.exec_command('sudo systemctl restart apache2')
            wait_for_ok_status_opencart(30)
    else:
        raise ConnectionError("Сервис недоступен, невозможно произвести перезагрузку сервисов.")
