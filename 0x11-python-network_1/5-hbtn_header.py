#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri july 05 07:02:53 2024

@author: Ernest Okiya
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    response = get(url)
    info = response.headers
    print(info.get('x-request-id'))
