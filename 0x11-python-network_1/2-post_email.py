#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

def post_email(url, email):
    """
    Sends a POST request to the specified URL with the provided email.
    Returns the decoded body of the response.
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        return body

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    result = post_email(url, email)
    print(result)
