#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the \
first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """prints titles of top ten got posts for a given subreddit
    Args:
    subreddit (string): name of given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers={"User-Agent": "globann"},
                     allow_redirects=False)
    if r.status_code == 200:
        for post in r.json()['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
