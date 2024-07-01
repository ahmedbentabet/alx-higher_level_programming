#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter using urllib.

Usage:
    ./post_request.py <URL> <email>
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the data
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')  # Encode the data to bytes

    # Send a POST request to the URL with the encoded data
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)
