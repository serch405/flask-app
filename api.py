from flask import Blueprint, request, abort, jsonify
from config import app, mail
from models import User


api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/user')
def get_user():
    email = request.args.get('email')
    user = User.query.filter_by(email=email).first()

    if user:
        user_data = {
            'username': user.username,
            'email': user.email,
        }
        return jsonify(user=user_data)
    else:
        abort(404)

@api_bp.route('/users')
def get_users():
    users = User.query.all()
    user_list = []

    if users:
        for user in users:
            user_data = {
                'username': user.username,
                'email': user.email,
            }
            user_list.append(user_data)
        return jsonify(users=user_list)
    else:
        abort(404)
