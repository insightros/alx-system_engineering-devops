#!/usr/bin/python3
"Exports to-do list information"
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks_list = [{
        "task": t.get("title"),
        "completed": t.get("completed"),
        "username": username
    } for t in todos]

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump([{str(user_id): tasks_list}], jsonfile)
