from flask import Flask
from flask_migrate import Migrate, upgrade
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from configparser import ConfigParser
import os


if __name__ == '__main__':
    app.run()

app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')
app.config['SECRET_KEY'] = config.get('flask', 'SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('flask', 'SQLALCHEMY_DATABASE_URI')
app.config['MAIL_SERVER'] = config.get('mail', 'MAIL_SERVER')
app.config['MAIL_PORT'] = config.get('mail', 'MAIL_PORT')
app.config['MAIL_USE_TLS'] = config.get('mail', 'MAIL_USE_TLS')
app.config['MAIL_USERNAME'] = config.get('mail', 'MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = config.get('mail', 'MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = config.get('mail', 'MAIL_DEFAULT_SENDER')

mail = Mail(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
