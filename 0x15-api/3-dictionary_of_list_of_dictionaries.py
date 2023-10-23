#!/usr/bin/python3
"""Exports to-do list info for a user to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": to.get("title"),
                "completed": to.get("completed"),
                "username": us.get("username")
            } for to in requests.get(url + "todos",
                                    params={"userId": us.get("id")}).json()]
            for us in users}, jsonfile)
