#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    
    # Fetch user information
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch user's to-do list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Create a list of dictionaries for each task
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Create a dictionary with the required format
    user_tasks = {str(user_id): tasks_list}

    # Write to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
