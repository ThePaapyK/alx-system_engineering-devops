#!/usr/bin/python3
"""for a given employee ID, returns information \
about his/her TODO list progress."""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url, params={"userId": argv[1]})
    r2 = requests.get(url2, params={"id": argv[1]})
    c = r.json()
    d = r2.json()
    with open(argv[1] + '.csv', 'w', newline='') as file:
        written = csv.writer(file, quoting=csv.QUOTE_ALL)
        for item in c:
            written.writerow([item['userId'], d[0]['username'],
                             item['completed'], item['title']])
