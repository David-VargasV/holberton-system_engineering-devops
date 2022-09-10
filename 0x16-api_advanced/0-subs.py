#!/usr/bin/python3
"""
How many subscribers?
"""

import imp
from wsgiref import headers
import requests


def number_of_subscribers(subreddit):
    """ Function that returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}.json'.format(subreddit)
    user = 'reddit_user'
    headers = {'User-Agent': user}

    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        return 0

    data = req.json()['data']
    p_list = data['children']
    p_data = p_list[0]['data']

    return p_data['subreddit_subscribers']
