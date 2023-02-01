#!/usr/bin/python3
"""queries the Reddit API and returns the number of \
subscribers (not active users, total subscribers) for \
a given subreddit. If an invalid subreddit is given, \
the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a subreddit
    Arg:
        subreddit (string): given subreddit
    Returns: number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers={"User-Agent": "globann"},
                     allow_redirects=False)
    if r.status_code == 200:
        return r.json()['data']['subscribers']
    return 0
