#!/bin/bash
# This script takes a URL, sends a GET request with a header, and displays the body of the response (A header variable X-School-User-Id must be sent with the value 98)
curl -s -H "X-School-User-Id: 98" "$1"
