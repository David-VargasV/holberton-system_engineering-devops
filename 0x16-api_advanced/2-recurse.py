#!/usr/bin/python3
"""
Recurse it!
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Write a recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user = 'reddit_user'

    if after:
        url += "?after={}".format(after)
    headers = {'User-Agent': user}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 404:
        return None
    data = req.json()['data']
    p_list = data['children']
    for p in p_list:
        count += 1
        hot_list.append(p['data']['title'])

    after = data['after']
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
