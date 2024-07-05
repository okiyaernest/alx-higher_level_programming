#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri july 05 07:02:53 2024

@author: Ernest Okiya
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    username = argv[2]
    repo = argv[1]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repo)
    response = get(url)
    try:
        objects = response.json()
        for i, obj in enumerate(objects):
            print('{}: {}'.format(obj.get('sha'),
                                  obj.get('commit').get('author')
                                  .get('name')))
            if i == 9:
                break
    except ValueError:
        pass
