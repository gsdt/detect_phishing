#!/usr/bin/python3

def getHost(url):
	l = url.split("/")
	if l[0].find("http") == -1:
		if l[0][:3] =="www":
			return (l[0][4:])
		else:
			return(l[0])
	else:
		return (l[2])
