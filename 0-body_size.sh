#!/bin/bash
# send a request to URL, and desplay the size of the body of the response
curl -s "$1" | wc -c
