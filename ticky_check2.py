#!/usr/bin/env python3

import sys
import re
import csv
import subprocess

# Number of error messages dictionary
error = {}

with open("syslog.log") as f:
    line = f.readline()
    while line != "":
        pattern = "(INFO|ERROR)([\w ']+)"  # (\[#[\d]+\])?\(([\w.]+)\)"
        result = re.search(pattern, line.strip())
        res = result[2].strip()
        if res not in error:
            error[res] = 1
        else:
            error[res] = error.get(res)+1

        line = f.readline()

# print(error.items())

with open("erreur_message.csv", "w", newline="") as csvfile:
    fieldnames = ['Error', 'Count']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
    for key, item in sorted(error.items(), key=lambda x: x[1], reverse=True):
        print(key, item)
        writer.writerow({"Error": key, "Count": item})
