#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
Handles the JSON response and displays the result appropriately.
"""

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    
    # Get the letter from the command line argument, or set q="" if no argument is given
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else: 
        q = ""

    # Prepare the payload for the POST request
    data = {'q': q}

    # Send a POST request to the URL with the letter as a parameter
    response = requests.post(url, data=data)

    try:
        # Attempt to parse the response as JSON
        json_response = response.json()
        if json_response:
            # If the JSON response is not empty, display the id and name
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            # If the JSON response is empty, display "No result"
            print("No result")
    except ValueError:
        # If the response body is not valid JSON, display "Not a valid JSON"
        print("Not a valid JSON")
