#!/usr/bin/python3
"""
Function that queries Reddit Api
"""

import requests


def top_ten(subreddit):
    """
    This method queries the reddit API and prints the first 10 hot posts
    for given reddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Asus-Vivobook/0.0.1'}
    query_params = {'limit': 10}

    response = requests.get(url, headers=headers, params=query_params
             allow_redirects=False)

    if response.status_code == 404:
        print(None)
    else:
        data = response.json()
        for post in data['data']['children'][:10]:
            print(post['data']['title'])
