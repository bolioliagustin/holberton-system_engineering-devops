#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles of all
hot articles for a given subreddit.
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], after=''):
    """
    recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 404:
        return None
    else:
        data = response.json().get('data').get('children')
        for i in range(len(data)):
            hot_list.append(data[i].get('data').get('title'))
        after = response.json().get('data').get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
