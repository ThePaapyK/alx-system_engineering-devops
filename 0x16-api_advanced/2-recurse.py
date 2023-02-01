#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns \
a list containing the titles of all hot articles for a given \
subreddit. If no results are found for the given \
subreddit, the function should return None."""

import requests


def recurse(subreddit, hot_list=[], _next=None):
    """returns titles of all hot articles of a subreddit
    Args:
    subreddit (string): name of given subreddit
    hot_list (list): titles of hot posts
    _next: after parameter of api lisiting"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={"User-Agent": "globann"},
                     allow_redirects=False,
                     params={'after': _next})
    if r.status_code == 200:
        _next = r.json()['data']['after']
        if _next is None:
            return hot_list

        for post in r.json()['data']['children']:
            hot_list.append(post['data']['title'])
        return recurse(subreddit, hot_list, _next)
    else:
        return None
