#!/bin/bash
# sends DELETE request to URL passed first argument,displays body of response
curl - s "$1" - X DELETE
