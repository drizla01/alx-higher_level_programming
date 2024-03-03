#!/usr/bin/python3
"""
Python script that takes URL, send the a request to the URL and display the value of
X-Request-id variable found in the header of the response
"""


if __name__ == "__main__":
    from sys import argv
    import urllib.request

    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
