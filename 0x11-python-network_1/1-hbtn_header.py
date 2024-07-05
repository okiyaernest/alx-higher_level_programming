#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri july 05 07:02:53 2024

@author: Ernest Okiya
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
