#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email parameter.
"""

import sys
import urllib.parse
import urllib.request


class PostEmail:
    """
    PostEmail class to handle sending email via POST request.
    """

    def send_post_request(self, url, email):
        """
        Sends a POST request to the specified URL with given email parameter.
        """
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))


# Usage example
if __name__ == "__main__":
    # Example URL and email
    example_url = "http://0.0.0.0:5050"
    example_email = "test@test.com"

    # Create an instance of the PostEmail class
    post_email_instance = PostEmail()

    # Send POST request
    post_email_instance.send_post_request(
        example_url, example_email
    )
