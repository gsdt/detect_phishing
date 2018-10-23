# from tldextract import extract
from bs4 import BeautifulSoup
import urllib.request
import string
import sys

def is_login(html_code):
    word ={"login","signin","enter","username","username or email address","email or phone number","password"}
    count_password=0
    count_text=0
    count_button =0
    
    soup = BeautifulSoup(html_code,"html.parser")
    for check in soup.find_all('input'):
        if check.get('type')=="password":
            count_password = count_password +1
        if check.get('type')=="text":
            count_text = count_text+ 1

    if count_password >0:
        count_form=0
        for t in soup.find_all('form'):
            count =0
            count_text1 =0
            count_form=count_form+1
            for check in t.find_all('input'):
                if check.get('type')=="password":
                    count = count +1
                if check.get('type')=='text':
                    count_text1 = count_text1+ 1
                if  check.get('type')=='email':
                    count_text1 = count_text1+ 1
            if count == 1 & count_text1 == 1 :
                return "LOGIN"
            else:
                return "REGISTER"
    else:
        return "NORMAL"


if __name__ == "__main__":
    html_code = open('code.html').read()
    is_login(html_code)