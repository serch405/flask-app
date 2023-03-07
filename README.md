# About the project
This Flask app was created as a test object for automated tests. It allows a logged-in user to download static files and showcases the usage of iFrames.

# Preconditions
1. Create a new virtual environment and activate it
 ```
python3 -m venv venv
.\venv\Scripts\activate
```
2. Install the required dependencies
```
pip install -r requirements.txt
```
3. Initialize the database
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
6. Fill `config.ini` based on `sample_config.ini`. Note that `MAIL_PASSWORD` property is not a regular Gmail password, it's a custom password for application (see https://support.google.com/accounts/answer/185833?hl=en)

# How to run Flask application in debug mode
```
flask --app main run --host=0.0.0.0 --debug
```

# How to access from the same pc
```
127.0.0.1:5000
```

# How to access from a different pc inside the same local network
```
<host_ip>:5000
```
