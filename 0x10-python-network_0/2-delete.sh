#!/bin/bash
# This script sends a DELETE request to the provided URL
# and displays the body of the response.

curl - s - X DELETE "$1"
