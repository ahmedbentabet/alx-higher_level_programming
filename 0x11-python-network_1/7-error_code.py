#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the HTTP status code is >= 400, prints Error code: followed
by the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the status code is >= 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the body of the response
        print(response.text)
