#!/usr/bin/python3

import config
import Helper
import sys
import os

# fblack = config.getBlackListPointer()
# fwhite = config.getWhiteListPointer()
# frandom = config.getRandomListPointer()

def createData():
    myConnection = config.getConnection()
    cursor = myConnection.cursor()

    fblack = open(config.BLACK_LIST, 'r')
    fwhite = open(config.WHITE_LIST, 'r')

    lsBlack = fblack.readlines()
    lsWhite = fwhite.readlines()
    # lsRandom = frandom.readlines()

    cnt = 0
    for x in lsBlack:
        cnt += 1
        l = x.split("|")
        sql = 'INSERT INTO LINKs(host,url,type,confirm_time)  VALUES ("%s","%s","DIRTY",NOW())'
        cursor.execute(sql %(l[0].strip(),l[1].strip()))
        myConnection.commit()
        if os.environ["FLASK_ENV"]=="development" and cnt == 5000:
            break
    print('insert BlackList Done!')

    cnt = 0
    for x in lsWhite:
        cnt += 1
        l = x.split("|")
        sql = 'INSERT INTO LINKs(host,url,type,confirm_time)  VALUES ("%s","%s","SAFE",NOW())'
        cursor.execute(sql %(l[0].strip(),l[1].strip()))
        myConnection.commit()
        if os.environ["FLASK_ENV"]=="development" and cnt == 5000:
            break
    print('insert WhiteList Done!')
    # for x in lsRandom:
    #     l = x.split("|")
    #     sql = 'INSERT INTO RandomList(host,url,confirm_time)  VALUES ("%s","%s",NOW())'
    #     cursor.execute(sql %(l[0].strip(),l[1].strip()))
    #     myConnection.commit()
    # print('insert RandomList Done!')

    myConnection.close()
    cursor.close()
    fblack.close()
    fwhite.close()

def insert_link(url,type):
    myConnection = config.getConnection()
    cursor = myConnection.cursor()

    host = Helper.getHost(url).strip()
    sql = 'INSERT INTO LINKs(host,url,type,confirm_time)  VALUES ("%s","%s","%s",NOW())'
    print(host)
    values = (host,url.strip(),type.strip())
    cursor.execute(sql %values)
    myConnection.commit()

    myConnection.close()
    cursor.close()

def insert_report(url,type,userIP):
    myConnection = config.getConnection()
    cursor = myConnection.cursor()

    host = Helper.getHost(url).strip()
    sql = 'INSERT INTO REPORT(host,url,UserIP,type,reported_time)  VALUES ("%s","%s","%s","%s",NOW())'
    values = (host,url.strip(),userIP,type.strip())
    cursor.execute(sql %values)
    myConnection.commit()

    myConnection.close()
    cursor.close()

def counter_report(url, type, userIP):
    myConnection = config.getConnection()
    cursor = myConnection.cursor()

    host = Helper.getHost(url).strip()
    sql = "select count(distinct (UserIP)) as cnt from REPORT where type = 'DIRTY' and host= '{0}'".format(host)
    cursor.execute(sql)
    result, =cursor.fetchone()    
    
    myConnection.close()
    cursor.close()
    return result

def search_host(host):
    myConnection = config.getConnection()
    cursor = myConnection.cursor()

    sql = "Select * From LINKs Where host ='"+host.strip()+"'"
    cursor.execute(sql)
    result =cursor.fetchall()
            
    myConnection.close()
    cursor.close()

    if (len(result)  == 0):
        return "NOT FOUND"
    else:
        return str(result[0][3])

if __name__ == '__main__':
    createData()