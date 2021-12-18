# !/usr/bin/python3
"""
Module for a functon that returns the number of subsribers in a subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers to a specified subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'itsmuriuki'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('Data')
        subsribers = data.get('subscribers')
        if data is not None and subsribers is not None:
            return  subsribers 
    return 0
