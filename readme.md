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