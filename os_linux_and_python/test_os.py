import argparse
import os
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--dir", default=".", type=str, help="Path to directory where to look for files")
parser.add_argument("--package", default="argparse", type=str, help="Name of package to define the version of")
args = parser.parse_args()


# 1. Сетевые интерфейсы (как тест, например что интерфейсу назначен верный IP и он вообще есть в системе, состояние линка и т.п.)
def get_ifconfig_info():
    ifconfig = subprocess.check_output(["ifconfig"], universal_newlines=True)
    print(ifconfig)


# 2. Маршрут по умолчанию
def get_default_route():
    def_route = subprocess.check_output(["route", "get", "default"], universal_newlines=True)
    print(f"\n# 2. Default route is:\n{def_route}")


# 3. Информацию о состоянии процессора
def processor_info():
    proc_info = subprocess.check_output(["system_profiler", "SPHardwareDataType"], universal_newlines=True).split("\n")
    print("\n# 3. Processor info:")
    print(proc_info[6])
    print(proc_info[7])
    print(proc_info[8])


# 4. Информацию о процессе
def get_process_info():
    process_info = subprocess.check_output(["ps", "aux", "|grep", "bash"], shell=True, universal_newlines=True)
    print(f"\n# 4. Bash process info:\n{process_info}")


# 5. Список всех процессов
def get_processes_list():
    print("\n# 5. List of processes are: ")
    print(subprocess.call("ps"))


# 6. Статистику работы сетевых интерфейсов
# 7. Статус работы какого либо сервиса

# 8. Состояние сетевого порта на сервере (TCP или UDP)
def get_tcp_info():
    tcp_info = subprocess.check_output(["netstat", "-ap", "tcp", "-n"], universal_newlines=True)
    print(f"\n# 8. TCP info: {tcp_info}")


# 9. Версию пакета (имя пакета передается как аргумент)
def get_package_version():
    package = args.package
    for name, module in sys.modules.items():
        if name == package and hasattr(module, '__version__'):
            print(f"\n# 9. Version of module '{name}' is: ", module.__version__)


# 10. Список в файлов в директории (указать директорию)
def get_file_list():
    dir_name = args.dir
    if os.path.exists(dir_name):
        print(f"\n# 10. List of files for directory: {dir_name}")
        for file in os.listdir(dir_name):
            if os.path.isfile(file):
                print(file)
    else:
        print("Such directory doesn't exist")


# 11. Текущую директорию
def get_current_directory():
    print(f"\n# 11. Current directory is {os.getcwd()}")


# 12. Версию ядра
def get_core_version():
    print(f"\n# 12. Core version is: {os.uname()[3]}")


# 13. Версию операционной системы
def get_os_version():
    print(f"\n# 13. OS version is: {os.uname()[2]}")


if __name__ == "__main__":
    get_ifconfig_info()
    get_default_route()
    processor_info()
    get_process_info()
    get_processes_list()
    get_tcp_info()
    get_package_version()
    get_file_list()
    get_current_directory()
    get_core_version()
    get_os_version()
