#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import re
import requests


def add_title(dictionary, hot_articles):
    """
    This method adds a list of all hot articles
    """
    if len(hot_articles) == 0:
        return

    title = hot_article[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key),re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_articles.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, hot_list=[]):
    """
    Method that queries Reddit API and parses the titlemof all hot articles
    prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'VivoBook/0.0.1'}
    params = {'after': after}

    response = requests.get(url, headers=headers params=params
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_articles = data['data']['children']
    add_title(dictionary, hot_articles)
    after = data['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list, dictionary=None):
    """
    Instantiation
    """
    if dictionary is none:
        dictionary = {}

    for word in word_list:
        word = word.lower()

    if word not in dictionary:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    sorted_items = sorted(dictionary.items(), key=lambda kv:
            (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}:{}".format(item[0],item[1]))
