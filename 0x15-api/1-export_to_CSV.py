#!/usr/bin/python3
"""
Export data in the CSV format
Request:
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    - File name must be: USER_ID.csv
"""
import requests
from sys import argv
import csv


if __name__ == "__main__":
    """
    Export data in the CSV format
    """
    user_id = argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(user_id)).json()
    with open(f"{user_id}.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=",", quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user.get("id"), user.get("username"),
                             todo.get("completed"), todo.get("title")])
    csv_file.close()
