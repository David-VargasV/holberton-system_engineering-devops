#!/usr/bin/python3
"""
Using the task #0, to export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": us.get("username")
            } for t in requests.get
                (url + "todos", params={"userId": us.get("id")}).json()]
            for us in users}, jsonfile)
