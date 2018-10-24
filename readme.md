# About this project
1. About
    Project for IAA
2. Thanks
    Nguyen Anh Tuan
    Nguyen Huu Dung
    Nguyen Quoc Anh
    Nguyen Xuan Hoa
    Nguyen Quang Dam
    Nguyen The Lam

# To run this project
1. Requirement
    - Linux (other OS version haven't been tested.)
    - Python 3
    - MySQL
2. Prepare for build project
    Please run these commands on bash:
    ```

    virtualenv venv
    . venv/bin/activate
    pip install Flask
    pip install mysql-connector-python
    pip install bs4
    ```

3. Run this project
    ```
    export FLASK_APP=app.py
    flask run
    ```

# To use api
1. Check URL (http://server:5000/api/phising)

    *Request*

        - type = `url`
        - contents = `fakesite.com`

    *Response*

        - error_code:
        - message:
        - result: `NOT FOUND/ DIRTY/ SAFE/ REPORTED`

2. Check html (http://server:5000/api/phising)

    *Request*

        - type = `html_code`
        - contents = `<html>...</html>`

    *Response*

        - error_code:
        - message:
        - result: `NOT LOGIN/ DIRTY/ SAFE`

3. Report (http://server:5000/api/report)

    *Request*

        - type = `DIRTY`
        - url = `fakebook.com`

    *Response*

        - error_code: `0 / 3`
        - message: `report success/ More than 10 people report this site`
        - counter : counter number of users report this site


