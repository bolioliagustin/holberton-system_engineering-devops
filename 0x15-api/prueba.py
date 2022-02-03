#!/usr/bin/python3

from sys import argv
import requests
import csv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    r = requests.get(url)
    user = r.json()
    """print (user)"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    r = requests.get(url)
    todos = r.json()
    print (todos)
