#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    site_Url = "https://jsonplaceholder.typicode.com/users"
    url = site_Url + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dict = {employeeId: []}
    for task in tasks:
        dict[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employeeId), 'w') as filename:
        json.dump(dict, filename)