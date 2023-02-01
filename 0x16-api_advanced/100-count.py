#!/usr/bin/python3
""""a recursive function that queries the Reddit API, \
parses the title of all hot articles, and prints a \
sorted count of given keywords (case-insensitive, delimited \
by spaces. Javascript should count as javascript, \
but java should not)."""
import requests


def count_words(subreddit, word_list, _next=None, count={}):
    """prints a sorted count of given keywords in api response
    Args:
        subreddit ([string]): given subreddit
        word_lists (list): list of keywords to be parsed
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={"User-Agent": "globann"},
                        allow_redirects=False,
                        params={'after': _next})
    if _next is None:
        for word in word_list:
            count[word] = 0

    if r.status_code == 200:
        _next = r.json()['data']['after']
        if _next is None:
            for word, value in count.items():
                if value != 0:
                    print('{}: {}'.format(word, value))
            return

        for post in r.json()['data']['children']:
            for word in word_list:
                string = post['data']['title']
                string_split = string.lower().split(' ')
                count[word] += string_split.count(word.lower())
                counts = sorted(count.items(), key=lambda x:x[1], reverse=True)
                count = dict(counts)
        return count_words(subreddit, word_list, _next, count)
    else:
        return
