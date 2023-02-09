#!/usr/bin/python3
"""Gets employee details"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    site_url = "https://jsonplaceholder.typicode.com/users"
    # getting the user todo's
    url = site_url + "/" + employeeId

    response = requests.get(url)
    emp_names = response.json().get('name')

    todo_Url = url + "/todos"
    response = requests.get(todo_Url)
    tasks = response.json()
    completed = 0
    completed_tasks = []

    for task1 in tasks:
        if task1.get('finished'):
            completd_tasks.append(task1)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_names, completed, len(tasks)))

    for task1 in completed_tasks:
        print("\t {}".format(task1.get('title')))
