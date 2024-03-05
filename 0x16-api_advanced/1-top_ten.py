#!/usr/bin/python3
""" function that queries the Reddit API"""

import requests


def top_ten(subreddit):
    """Prints the first 10 hot posts on a given Reddit subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'VivoBook/0.0.1'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
