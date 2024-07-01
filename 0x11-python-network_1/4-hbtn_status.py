#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using requests.

Displays information about the response including type and content.
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content).__name__}")
    print(f"\t- content: {content}")
