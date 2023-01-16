#!/usr/bin/python3
"""for a given employee ID, returns information \
about his/her TODO list progress."""
from sys import argv
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/{}".format(argv[1])
    url2 = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    r = requests.get(url)
    r2 = requests.get(url2)
    c = r.json()
    d = r2.json()
    n = 0
    for item in c:
        if item['completed'] is True:
            n = n + 1
    print("Employee {} is done with \
           tasks({}/{}):".format(d['name'], n, len(c)))
    for todo in c:
        print("\t {}".format(todo['title']))
