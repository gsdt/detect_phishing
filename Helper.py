#!/usr/bin/python3

from urllib.parse import urlparse
import sys


def getHost(url):
	parser = urlparse(url)
	return parser.hostname

if __name__ == "__main__":
	print(getHost("https://docs.python.org/3/library/urllib.parse.html"))
	
