#!/usr/bin/python3
"""
Export all data in the JSON format.
"""


import json
import requests


if __name__ == '__main__':
    """
    Export all data in the JSON format.
    """
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        verify=False).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         verify=False).json()
    user_dict = {}
    name_dict = {}
    for id in user:
        user_id = id.get('id')
        user_dict[user_id] = []
        name_dict[user_id] = id.get('username')

    for task in todos:
        user_id = task.get("userId")
        task_dic = {}
        task_dic["task"] = task.get("title")
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = name_dict.get(user_id)
        user_dict.get(user_id).append(task_dic)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_dict, json_file)
    json_file.close()
