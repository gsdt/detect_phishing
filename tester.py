import requests

url = "http://35.190.183.74:5000/api/phishing"
url_report = "http://35.190.183.74:5000/api/report"


r = requests.Session()

html_code = open("code.html", "r").read()

data = {
    'type' : 'html_code',
    'contents': html_code
}
# test detect phishing
response = r.post(url, data=data).text

# test report phishing
# response = r.post(url_report, data={'type' :'DIRTY', 'url': 'fake.com'}).text
print(response)