#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id header from a URL using urllib.

Usage:
    ./1-hbtn_header.py <URL>
"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a request to the URL
    with request.urlopen(url) as response:
        # Get the value of X-Request-Id header using .get()
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
