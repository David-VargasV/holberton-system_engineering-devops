#!/usr/bin/python3
"""
Using the task #0, to export data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/{}".format(userId)).json()
    todo = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), 'w', newline='') as jsonile:
        json.dump({userId: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": user.get("username")
        } for t in todo]}, jsonile)
