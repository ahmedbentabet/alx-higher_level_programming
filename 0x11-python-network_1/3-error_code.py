#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the
response (decoded in utf-8).
Handles HTTPError exceptions and prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Print the error code if an HTTPError occurs
        print(f"Error code: {e.code}")
