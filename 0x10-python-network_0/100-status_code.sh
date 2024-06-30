#!/bin/bash
# Script to display only the status code of a URL response
curl -s -o /dev/null -w "%{http_code}" "$1"
