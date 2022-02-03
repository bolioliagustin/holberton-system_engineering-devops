#!/usr/bin/python3
""" Export data in the CSV format """


import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id), verify=False).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id), verify=False).json()
    with open("{}.csv".format(user_id), "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user.get("id"), user.get("username"),
                             todo.get("completed"), todo.get("title")])

