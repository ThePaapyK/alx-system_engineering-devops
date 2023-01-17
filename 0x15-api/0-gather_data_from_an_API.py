#!/usr/bin/python3
"""for a given employee ID, returns information \
about his/her TODO list progress."""
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url, params={"userId": argv[1]})
    r2 = requests.get(url2, params={"id": argv[1]})
    c = r.json()
    d = r2.json()
    n = 0
    for item in c:
        if item['completed'] is True:
            n = n + 1
    print("Employee {} is done with tasks({}/{}):".format(d[0]['name'],
                                                          n, len(c)))
    for todo in c:
        if todo['completed'] is True:
            print("\t {}".format(todo['title']))
