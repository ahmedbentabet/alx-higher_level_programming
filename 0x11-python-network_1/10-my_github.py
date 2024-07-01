#!/usr/bin/python3
"""
Uses GitHub API to display user id using Basic Authentication
with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    # Send a GET request to the GitHub API with Basic Authentication
    response = requests.get(url, auth=(username, token))

    # Parse the JSON response
    json_response = response.json()
    # Print the user id if available, otherwise print None
    print(json_response.get("id"))
