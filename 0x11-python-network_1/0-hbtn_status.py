#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status using urllib.

Displays information about the response including type, content in bytes,
and UTF-8 decoded content.
"""
from urllib import request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
    print(f"\t- utf8 content: {utf8_content}")
