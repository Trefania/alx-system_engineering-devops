#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        all_sub = 0
    else:
        all_sub = response.json().get('data').get('subscribers')

        return all_sub