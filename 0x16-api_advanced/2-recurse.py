#!/usr/bin/python3

"""
returns a list containing the titles of all hot articles
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
    """
    url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        my_data = response.json().get("data").get("after")
        if my_data is not None:
            after = my_data
            recurse(subreddit, hot_list)
        titles = response.json().get("data").get("children")
        for tittle in titles:
            hot_list.append(tittle.get("data").get("title"))
        return hot_list
    else:
        return (None)
