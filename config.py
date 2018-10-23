#!/usr/bin/python3
import mysql.connector

def getConnection():
	hostname = 'localhost'
	username = 'gsdt'
	password = '0903'
	database = 'PhishURL'
	myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
	return myConnection

BLACK_LIST = "raw_data/TotalBlackList.txt"
WHITE_LIST = "raw_data/opendns-top-domains.txt"


# def getBlackListPointer():
# 	return open("/home/neo/Desktop/IAADatabase/Databases/TotalBlackList.txt","r")

# def getWhiteListPointer():
# 	return open("/home/neo/Desktop/IAADatabase/Databases/opendns-top-domains.txt","r")
	
# def getRandomListPointer():
# 	return open("/home/neo/Desktop/IAADatabase/Databases/opendns-random-domains.txt","r")