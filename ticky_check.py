#!/usr/bin/env python3

import sys
import re
import csv

# Number of error messages dictionary
error = {}  # "Error": count
# Number of inputs of each user
per_user = {}  # "username": {"INFO": 0, "ERROR": 0}


def create_csv_user():
    with open("syslog.log") as f_user:
        line = f_user.readline()
        while line != "":
            pattern = "(INFO|ERROR)[\w\d \[\]#']*\(([\w.]+)\)"
            result = re.search(pattern, line)
            info = 0
            error = 0
            username = result.group(2)
            if username not in per_user:
                if result.group(1) == "INFO":
                    info = 1
                if result.group(1) == "ERROR":
                    error = 1
                per_user[username] = {'INFO': info, 'ERROR': error}
            else:
                res = per_user[username]
                #print("result: ", res)
                if result.group(1) == "INFO":
                    info = res.get("INFO")+1
                else:
                    info = res.get("INFO")

                if result.group(1) == "ERROR":
                    error = res.get("ERROR")+1
                else:
                    error = res.get("ERROR")
                per_user[username] = {'INFO': info, 'ERROR': error}

            line = f_user.readline()
    f_user.close()

    with open("user_statistics.csv", "w", newline="") as csvfile:
        fieldnames = ['Username', 'INFO', "ERROR"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key, item in sorted(per_user.items()):
            print(key, item["INFO"], item["ERROR"])
            writer.writerow(
                {"Username": key, "INFO": item["INFO"], "ERROR": item["ERROR"]})


def create_csv_error():
    with open("syslog.log") as f_error:
        line = f_error.readline()
        while line != "":
            pattern2 = "(INFO|ERROR)([\w ']+)"
            result = re.search(pattern2, line.strip())
            res = result.group(2).strip()
            if res not in error:
                error[res] = 1
            else:
                error[res] = error.get(res)+1

            line = f_error.readline()
    f_error.close()

    # print(error.items())

    with open("error_message.csv", "w", newline="") as csvfile:
        fieldnames = ['Error', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        for key, item in sorted(error.items(), key=lambda x: x[1], reverse=True):
            print(key, item)
            writer.writerow({"Error": key, "Count": item})


create_csv_user()
create_csv_error()
