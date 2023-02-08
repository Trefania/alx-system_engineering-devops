#!/usr/bin/python3
"""Gets employee details"""

from requests import get
from sys import argv


if __name__ == "__main__":
    site_url = "https://jsonplaceholder.typicode.com"

    todos_url = site_url + "/user/{}/todos".format(argv[1])
    user_todo = get(todos_url).json()
    user_url = site_url + "/users/{}".format(argv[1])
    user_dits = get(user_url).json()

    username = user_dits.get("name")
    total_tasks = len(user_todo)
    finished_task_titles = [user.get("title")
                             for user in user_todo if user.get("completed")]
    finished_tasks = len(finished_task_titles)
    message = "Employee {} is done with tasks({}/{}):".format(
        username, finished_tasks, total_tasks)
    print("{}".format(message))
    for todo in finished_task_titles:
        print("\t {}".format(todo))