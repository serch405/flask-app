# About the project
This Flask app was created as a test object for automated tests. It allows a logged-in user to download static files and showcases the usage of iFrames.

# Preconditions
1. Create a new virtual environment and activate it
 ```
python3 -m venv venv
```
2. Activate a virtual environment
on Windows:
```
.\venv\Scripts\activate
```
on Linux:
```
source venv/bin/activate
```
2. Install the required dependencies
```
pip install -r requirements.txt
```
3. Create `config.ini` inside the project folder. It should be based on `sample_config.ini`. Note that `MAIL_PASSWORD` property is a custom password for application (see https://support.google.com/accounts/answer/185833?hl=en)
4. Initialize the database
```
flask --app main db init
```
4. Generate a migration script based on Database models
```
flask --app main db migrate
```
5. Apply the migration to your database
```
flask --app main db upgrade
```

# How to run Flask application in a development environment
```
flask --app main run --host=0.0.0.0 --debug
```

# How to run Flask application in a production environemnt
1. Install a web server (e.g. Nginx)
2. Configure the web server to act as a reverse proxy for the application
3. Run the application
```
gunicorn main:app -b 0.0.0.0:8080
```

# How to run all tests
```
pytest
```
