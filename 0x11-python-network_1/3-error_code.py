#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri july 05 07:02:53 2024

@author: Ernest Okiya
"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
