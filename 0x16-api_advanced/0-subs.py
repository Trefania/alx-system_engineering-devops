#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)

    if (response.json().get('error')) is not None:
        return 0
    elif response.json().get('data').get('subscribers') is None:
        return 0
    else:
        return response.json().get('data').get('subscribers')
    