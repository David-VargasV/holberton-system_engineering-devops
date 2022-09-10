#!/usr/bin/python3
"""
Top Ten
"""

import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot
    posts listed for a given subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user = 'reddit_user'
    headers = {'User-Agent': user}

    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code == 404:
        print('None')
    else:
        data = req.json()['data']
        p_list = data['children']

        for p in p_list[0:10]:
            print(p['data']['title'])
