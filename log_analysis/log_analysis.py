import argparse
import json
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='path', action='store', required=True, help='Path to logfile')

args = parser.parse_args()
log_files = []

if os.path.isfile(args.path) and os.path.splitext(args.path)[1] == ".log":
    # если в аргументе передан путь до конкретного .log-файла, то анализ будет проведен только по этому файлу
    log_files.append(args.path)
elif os.path.isdir(args.path):
    # если в аргументе передан путь до директории, то анализ будет проведен по всем файлам из этой директории
    # с расширением .log
    log_files = [args.path + f for f in os.listdir(args.path) if f.endswith('.log')]
else:
    # если путь указан некорректно, или файл имеет расширение, отличное от .log, выбрасываем ошибку.
    raise TypeError("Такой директории или файла не существует, или файл не является .log-файлом.")

# не смогла запихать это условие в elif выше
if len(log_files) == 0:
    raise TypeError("В переданной директории отсутствуют .log-файлы.")

results = []  # список словарей по принципу 1 словарь = 1 файл с логами
for log_file in log_files:
    try:
        with open(log_file) as f:
            result = {"file": f.name}
            result["GET"] = 0
            result["POST"] = 0
            result["PUT"] = 0
            result["DELETE"] = 0
            result["HEAD"] = 0
            result["OPTIONS"] = 0

            ips = {}
            long_reqs = []
            client_error_reqs = []
            server_error_reqs = []
            for index, line in enumerate(f.readlines()):
                # print(line)

                method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD|OPTIONS)", line)
                if method:
                    method = method.groups()[0]
                    result[method] += 1
                else:
                    method = ""

                ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                if ip and ip.group() in ips.keys():
                    ip = ip.group()
                    ips[ip] += 1
                elif ip:
                    ip = ip.group()
                    ips[ip] = 1
                else:
                    ip = ""

                # топ 10 самых долгих запросов,
                # должно быть видно метод, url, ip, время запроса
                req_url = re.search(r"\" \d{3} \d+ \"(.+)\" ", line).groups()[0]
                req_time = re.search(r"\" \d{3} (\d+)", line).groups()[0]
                long_req = [method, req_url, ip, req_time]
                long_reqs.append(long_req)

                # - топ 10 запросов, которые завершились клиентской ошибкой,
                # должно быть видно метод, url, статус код, ip адрес
                c_status = re.search(r"\" (4\d{2})", line)
                if c_status and len(client_error_reqs) < 10:
                    c_status = c_status.groups()[0]
                    client_error_reqs.append({"method": method,
                                              "url": req_url,
                                              "status": c_status,
                                              "ip": ip
                                              })


                # - топ 10 запросов, которые завершились ошибкой со стороны сервера,
                # должно быть видно метод, url, статус код, ip адрес
                s_status = re.search(r"\" (5\d{2})", line)
                if s_status and len(server_error_reqs) < 10:
                    s_status = s_status.groups()[0]
                    server_error_reqs.append({"method": method,
                                              "url": req_url,
                                              "status": s_status,
                                              "ip": ip
                                              })

            # сортируем список ip по количеству отправленных запросов по убыванию
            # и добавляем в результат по файлу только первые 10 ip с максимальным количеством запросов
            list_ips = list(ips.items())
            list_ips.sort(key=lambda i: i[1])
            list_ips.reverse()
            new_list_ips = []
            for ind, item in enumerate(list_ips):
                new_list_ips.append(item[0])
                if ind == 9:
                    break
            result["top_10_ips"] = new_list_ips

            # сортируем список с длинными запросами по убыванию
            # и формируем новый список из 10 первых словарей (1 словарь = 1 запрос)
            long_reqs.sort(key=lambda i: int(i[3]))
            long_reqs.reverse()
            new_long_reqs = []
            for ind, item in enumerate(long_reqs):
                new_long_reqs.append({"method": item[0],
                                       "url": item[1],
                                       "ip": item[2],
                                       "time": item[3]
                                       })
                if ind == 9:
                    break

            # добавляем информацию по самым длинным запросам,
            # по топ-10 запросов с клиентской ошибкой,
            # по топ-10 запросов с серверной ошибкой
            # и по общему количеству запросов
            # в результат по файлу
            result["top_10_long_reqs"] = new_long_reqs
            result["top_10_client_error_reqs"] = client_error_reqs
            result["top_10_server_error_reqs"] = server_error_reqs
            result["total_number_of_requests"] = index + 1

            # добавляем результат по файлу в общие результаты анализа
            results.append(result)

    # если не удалось открыть файл для чтения, печатаем ошибку
    except IOError as e:
        print(e)

    # записываем результаты в .json-файл
    with open("log_analysis/log_analysis_results.json", 'w') as r_file:
        json.dump(results, r_file, indent=4)
