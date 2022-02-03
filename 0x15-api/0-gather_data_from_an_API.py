#!/usr/bin/python3
""" script that using an API, for a given employee ID, returns information """


import requests
import json
from sys import argv

if __name__ == "__main__":
    """
    script that using an API, for a given employee
    ID, returns information
    """
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()
    name = user.get('name')
    tasks = []
    for task in todos:
        tasks.append(task.get('completed'))
    tasks_done = len([task for task in tasks if task])
    tasks_total = len(tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasks_done, tasks_total))
    for task in todos:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
