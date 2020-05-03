import argparse
import json
import os


parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='path',  action='store', required=True, help='Path to logfile')

args = parser.parse_args()
log_files = []

if os.path.isfile(args.path):
    log_files.append(args.path)
    print(log_files)
elif os.path.isdir(args.path):
    log_files = [args.path + f for f in os.listdir(args.path) if f.endswith('.log')]
    print(log_files)
else:
    raise TypeError("Такой директории или файла не существует")

if len(log_files) > 0:
    results = []
    for log_file in log_files:
        try:
            with open(log_file) as f:
                # print("открыли файл")
                result = {"file": f.name}
                results.append(result)
                # print(json.dumps(result, indent=4))
        except IOError as e:
            print(e)

    print(json.dumps(results, indent=4))
    with open("log_analysis/log_analysis_results.json", 'w') as r_file:
        json.dump(results, r_file, indent=4)
