#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    site_Url = "https://jsonplaceholder.typicode.com/users"
    url = site_Url + "/" + employeeId

    response = requests.get(url)
    emp_name = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    finished_tasks = []

    for task in tasks:
        if task.get('completed'):
            finished_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, done, len(tasks)))

    for task in finished_tasks:
        print("\t {}".format(task.get('title')))
