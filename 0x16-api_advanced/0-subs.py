#!/usr/bin/python3
"""
Function that queries the Reddit API for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This Method returns the number od subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'AsusVivobook/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
