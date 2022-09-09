#!/usr/bin/python3
"""
Script for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todo = requests.get(url + "todos", params={"userId": userId}).json()

    completed = [task.get("title") for task in todo if
                 task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(x)) for x in completed]
