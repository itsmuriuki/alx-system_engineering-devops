#!/usr/bin/python3
"""
Ping a RO-Do API for data on a specified user and saves the data to a csv file
"""

import csv
import requests
from sys import argv

from requests.sessions import TooManyRedirects

if __name__ == '__main__':
    employee_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(url_todo, params={'userId': employee_id})
    user = requests.get(url_user, params={'id': employee_id})

    todo_dict_list = todo.json()
    user_dict_list = user.json()

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "a+") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for tasks in todo_dict_list:
            status = tasks['completed']
            title = tasks['title']
            csvwriter.writerow(["{}".format(employee_id),
                                "{}".format(employee),
                                "{}".format(status),
                                "{}".format(title)])