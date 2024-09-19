#!/usr/bin/python3
"""Gather data from an API"""
import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_ID = sys.argv[1]
    userId_in_todos = {'userId': EMPLOYEE_ID}
    userId_in_users = {'id': EMPLOYEE_ID}

    r1 = requests.get(
                    "https://jsonplaceholder.typicode.com/todos",
                    params=userId_in_todos
    )
    r2 = requests.get(
                    "https://jsonplaceholder.typicode.com/users",
                    params=userId_in_users
    )

    r2_EMPLOYEE_dict = r2.json()[0]
    EMPLOYEE_NAME = r2_EMPLOYEE_dict['name']

    r1_list_of_dict = r1.json()
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    DONE_TASKS_TITLE = []

    for dict in r1_list_of_dict:
        if dict['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
            DONE_TASKS_TITLE.append(dict['title'])

        TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done \
    with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for done_task_title in DONE_TASKS_TITLE:
        print(f"\t {done_task_title}")
