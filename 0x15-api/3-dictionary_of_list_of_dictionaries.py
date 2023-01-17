#!/usr/bin/python3
"""for a given employee ID, returns information \
about his/her TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    r2 = requests.get(url2)
    d = r2.json()
    written = {}
    for user in d:
        list_ = []
        c = requests.get(url, params={'userId': user['id']}).json()
        for item in c:
            list_.append({
                            'username': user['username'],
                            'task': item['title'],
                            'completed': item['completed']})

        written[user['id']] = list_
        with open('todo_all_employees.json', 'w') as file:
            json.dump(written, file)
