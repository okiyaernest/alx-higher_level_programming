#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri july 05 07:02:53 2024

@author: Ernest Okiya
"""
from requests import get


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = get(url)
    bytes_content = response.text
    string = 'Body response:\n\t- type: {}\n\t- content: {}'.format(
             type(bytes_content), bytes_content)
    print(string)
