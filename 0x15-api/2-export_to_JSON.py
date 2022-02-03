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
    tasks = []
    for task in todos:
        tasks.append({'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': user_name})
    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump({user_id: tasks}, json_file)
    json_file.close()
