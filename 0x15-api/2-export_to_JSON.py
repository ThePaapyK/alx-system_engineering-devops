#!/usr/bin/python3
"""for a given employee ID, returns information \
about his/her TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url, params={"userId": argv[1]})
    r2 = requests.get(url2, params={"id": argv[1]})
    c = r.json()
    d = r2.json()
    written = {}
    list_ = []
    for item in c:
        list_.append({
                        'task': item['title'],
                        'completed': item['completed'],
                        'username': d[0]['username']})

    written[item['userId']] = list_
    with open(str(argv[1]) + '.json', 'w') as file:
        json.dump(written, file)
