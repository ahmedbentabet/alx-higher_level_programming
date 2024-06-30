#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes
curl -s "$1" | wc -c
