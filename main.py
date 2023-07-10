from flask import Flask, render_template, request, url_for, redirect, abort, flash, session, send_from_directory, jsonify
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from config import app, db, mail
from api import api_bp
from models import User
from datetime import datetime


app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repass = request.form['repass']
        
        if password != repass:
            flash('Passwords don\'t match')
            return redirect(url_for('register'))
            
        user_found_by_username = User.query.filter_by(username=username).first()
        user_found_by_email = User.query.filter_by(email=email).first()

        if user_found_by_username or user_found_by_email:
            flash('Username or Email already exists')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please login')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        
        if user is None:
            flash('User with such email doesn\'t exist')
            return redirect(url_for('login'))

        session['email'] = email
        verification_code = str(random.randint(100000, 999999))
        msg = Message('Verification Code', recipients=[email])
        msg.body = f'Hello, here is your verification code: {verification_code}'
        mail.send(msg)
        session['verification_code'] = verification_code
        return redirect(url_for('verify'))
    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    email = session.get('email')

    if not email:
        return redirect(url_for('login'))

    if request.method == 'POST':
        password = request.form['password']
        code = request.form['code']
        user = User.query.filter_by(email=email).first()

        if code != session.get('verification_code'):
            flash('Invalid password or code')
            return render_template('verify.html', email=email)

        if not check_password_hash(user.password, password):
            flash('Invalid password or code')
            return render_template('verify.html', email=email)
        session['username'] = user.username
        session.pop('verification_code', None)
        return redirect(url_for('dashboard'))
    return render_template('verify.html', email=email)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/iframe')
def iframe():
    current_time = datetime.now()
    return render_template('iframe.html', current_time=current_time)

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory('static', filename)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.before_request
def require_login():
    not_allowed_routes = ['dashboard', 'static', 'iframe']
    if request.endpoint in not_allowed_routes and 'username' not in session:
        return redirect(url_for('login'))
