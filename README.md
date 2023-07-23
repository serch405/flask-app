# About the project
This Flask app was created as a test object for automated tests. It allows a logged-in user to download static files and showcases the usage of iFrames.

# Preconditions
1. Create a new virtual environment
```
python3 -m venv venv
```
2. Activate the virtual environment

on Windows:
```
.\venv\Scripts\activate
```
on Linux:
```
source venv/bin/activate
```
3. Go to the project directory
4. Install required dependencies
```
pip install -r requirements.txt
```
5. Add `config.ini`, it should contain the same list of properties as in `sample_config.ini`
6. Fill `config.ini`, where `MAIL_PASSWORD` property is a custom password for application, see https://support.google.com/accounts/answer/185833?hl=en
7. Initialize the database
```
flask --app main db init
```
8. Generate a migration script based on Database models
```
flask --app main db migrate
```
9. Apply the migration to your database
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

# Run unit tests and measure the coverage
```
pytest --cov=main
```
