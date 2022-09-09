#!/usr/bin/python3
"""
Using the task #0, to export data in the CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todo = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
