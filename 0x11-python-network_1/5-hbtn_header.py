#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id variable
in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Get the value of the X-Request-Id header
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value
    print(x_request_id)
