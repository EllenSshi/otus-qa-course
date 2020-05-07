import time

import paramiko
import requests


host = "192.168.56.101"
user = "user"
secret = "admin"
port = 22


def get_request_status(hostname: str) -> int:
    return requests.get(f"http://{hostname}/opencart/").status_code


def get_ssh_client():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    return client


def wait_for_ok_status_opencart(timeout: int):
    t = 0
    while t <= timeout:
        if get_request_status(host) == 200:
            print(t)
            break
        else:
            time.sleep(1)
            t += 1
        if t == 30:
            raise AssertionError(f"Сервис недоступен, timeout={timeout}")


def test_reboot_and_check():
    if get_request_status(host) == 200:
        client = get_ssh_client()
        client.exec_command('sudo reboot')
        wait_for_ok_status_opencart(30)
    else:
        raise ConnectionError("Сервис недоступен, невозможно произвести перезагрузку.")


def test_reboot_services_and_check():
    if get_request_status(host) == 200:
        client = get_ssh_client()
        client.exec_command('sudo systemctl restart mysql.service')
        client.exec_command('sudo systemctl restart apache2')
        wait_for_ok_status_opencart(30)
    else:
        raise ConnectionError("Сервис недоступен, невозможно произвести перезагрузку сервисов.")
