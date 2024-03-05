#!/usr/bin/python3
"""
Function that queries the Reddit API for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This Method returns the number od subscribers for a given subreddit
    if invalid subreddit is given it returns 0
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Asus-Vivobook/0.0.1'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0

    if resposnse.status_code != 200:
        raise Exception(f'Error: {response.status_code}')

    data = response.json()
    return data['data']['subscribers']
