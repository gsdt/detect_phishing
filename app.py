#!/usr/bin/python3
from flask import Flask
from flask import request
from flask import jsonify

from bs4 import BeautifulSoup
from lam import HtmlData

import xml.etree.ElementTree as ET

import Database
import Helper
import mysql.connector
import site_type

app = Flask(__name__)

def detect_url(url):
    host = Helper.getHost(url)
    result = Database.search_host(host)
    res = dict()
    if(result == 'NOT FOUND'):
        return jsonify({
            'error_code': 1,
            'message': 'this url not in our database. please send the html_code to server',
            'result': result
        })
    else:
        return jsonify({
            'error_code': 0,
            'message': 'found this url in our database',
            'result': result
        })

    return jsonify(res)

def search(html_code):
    tree = ET.parse('searching.xml')
    root = tree.getroot()

    data = HtmlData()
    all_sentense = data.get_sentense(html_code)

    for sentense in all_sentense:
        for child in root:
            url = child.find('url').text
            string = child.find('string').text

            if(string in sentense):
                return url

    return "NOT FOUND"

def detect_html_code(html_code):
    if site_type.is_login(html_code) == 'LOGIN':
        result = search(html_code)
        if(result == 'NOT FOUND'):
            return jsonify({
                'error_code': 0,
                'message': "we didn't found any bad things",
                'result': 'SAFE'
            })
        else:
            return jsonify({
                'error_code': 0,
                'message': result,
                'result': 'DIRTY'
            })
    else:
        return jsonify({
            'error_code': 2,
            'message': 'This is not a login site.',
            'result': 'SAFE'
        })


@app.route('/api/phishing', methods=['POST'])
def phishing():
    dataType = request.form['type']
    contents = request.form['contents']
    if(dataType == 'url'):
        return detect_url(contents)
    if(dataType == 'html_code'):
        return detect_html_code(contents)

@app.route('/api/report', methods=['POST'])
def report():
    counter = Database.insert_report(request.form['url'],request.form['type'],request.remote_addr)
    if counter >= 10:
        return jsonify({
            'error_code': 3,
            'message' : 'More than 10 people report this site',
            'counter' : counter
        })
    return jsonify({
        'error_code': 0,
        'message' : 'report success',
        'counter' : counter
    })


