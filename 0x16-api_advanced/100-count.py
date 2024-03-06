#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import re
import requests


def add_title(dictionary, hot_articles):
    """
    This method adds a list of all hot articles to the dictionary
    """
    if not hot_articles:
        return dictionary

    hot_article = hot_articles[0]
    title = hot_article['data']['title'].lower().split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] = dictionary.get(key, 0) + 1
    hot_articles.pop(0)
    return add_title(dictionary, hot_articles)


def recurse(subreddit, after=None):
    """
    Method that queries Reddit API and parses the titlemof all hot articles
    prints a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'VivoBook/0.0.1'}
    params = {'after': after} if after else None

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    dictionary = {}
    dictionary = add_title(dictionary, data['data']['children'])
    return dictionary


def count_words(subreddit, word_list):
    """
    Instantiation
    """
    dictionary = {}
    for word in word_list:
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 0

    recurse_result = recurse(subreddit)
    if recurse_result:
        for key, value in recurse_result.items():
            if key in dictionary:
                dictionary[key] += value
    if not recurse_result or all(value == 0 for value in dictionary.values()):
        print("No results found")
        return

    sorted_items = sorted(dictionary.items(), key=lambda kv: (-kv[1], kv[0]))
    for item in sorted_items:
        if item[1] > 0:
            print("{}:{}".format(item[0], item[1]))
