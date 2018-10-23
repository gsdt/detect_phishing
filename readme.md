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
1. Check URL
    *Request*
        -   type = `url`
        -   contents = `fakesite.com`
    *Response*
        -   error_code:
        -   message:
        -   result: `NOT FOUND/ DIRTY/ SAFE`
2. Check html
    *Request*
        -   type = `html_code`
        -   contents = `<html>...</html>`
    *Response*
        -   error_code:
        -   message:
        -   result: `NOT LOGIN/ DIRTY/ SAFE`
3. Report
    *Request*
        -   type = `DIRTY`
        -   url = `fakebook.com`
    *Response*
        -   error_code: `0 / 3`
        -   message: `report success/ More than 10 people report this site`
        -   counter : counter number of users report this site