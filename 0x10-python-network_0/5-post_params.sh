#!/bin/bash
# This script takes a URL, sends a POST request with email and subject variables, and displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
