from flask import Blueprint, request, abort, jsonify
from models import User
from werkzeug.security import generate_password_hash
from config import app
from flask_restx import Api, Resource


api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp, version='1.0', title='My API', description='My API documentation using Swagger')


@api_bp.errorhandler(400)
def custom400(error):
    response = jsonify({'message': error.description['message']})
    return response, 400

@api.route('/user')
class User(Resource):
    @api.doc(description='Get a user by email')
    def get(self):
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

@api.route('/users')
class Users(Resource):
    @api.doc(description='Get all users')
    def get(self):
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

@api.route('/register', methods=['POST'])
class Register(Resource):
    @api.doc(description='Register a new user')
    def post(self):
        username = request.args.get('username')
        email = request.args.get('email')
        password = request.args.get('password')
        repass = request.args.get('repass')
            
        if password != repass:
            abort(400, {'message': 'Passwords don\'t match'})
                
        user_found_by_username = User.query.filter_by(username=username).first()
        user_found_by_email = User.query.filter_by(email=email).first()
        if user_found_by_username or user_found_by_email:
            abort(400, {'message': 'Username or Email already exists'})

        new_user = User(username=username, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()

        return "Success", 200
