#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter and displays the
body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the payload for the POST request
    data = {'email': email}

    # Send a POST request to the URL with the email as a parameter
    response = requests.post(url, data=data)

    # Display the body of the response (decoded in utf-8)
    print(response.text)
