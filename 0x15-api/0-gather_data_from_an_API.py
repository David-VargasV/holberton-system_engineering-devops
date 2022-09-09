#!/usr/bin/python3
"""
Script for a given employee ID, returns information
about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1]), verify=False).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()
    
    completed = []
    for task in todo:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed))
