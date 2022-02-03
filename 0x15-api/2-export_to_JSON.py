#!/usr/bin/python3
"""
Export data in the JSON format.
"""


import json
import requests
from sys import argv


if __name__ == '__main__':
    """
    Export data in the JSON format.
    """
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id), verify=False).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id}, verify=False).json()
    user_name = user.get('username')
    tasks = [task for task in todos]
    dict1 = {argv[1]: []}
    for task in tasks:
        dict2 = {'task': task.get('title'),
                 'completed': task.get('completed'),
                 'username': user_name}
        dict1[argv[1]].append(dict2)
    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(dict1, json_file)
    json_file.close()
