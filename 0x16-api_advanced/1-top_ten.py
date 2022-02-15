#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first 10
hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API
    and prints the titles of the first 10
    hot posts listed for a given subreddit.
    """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 404:
        print("None")
    else:
        data = response.json().get('data').get('children')
        for i in range(10):
            print(data[i].get('data').get('title'))
