#!/bin/bash
# This script takes a URL, sends a DELETE request, and displays the body of the response
curl -s -X DELETE "$1"
