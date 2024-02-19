#!/usr/bin/python3
"""
Script using REST API to get TO DO list for users
"""

import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    response = requests.get(url)
    employee_name = response.json().get("name")

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get("completed"):
            done_tasks.append(task.get("title"))
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task))
