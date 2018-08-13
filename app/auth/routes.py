from flask.views import MethodView
from flask import jsonify, request, Blueprint, make_response
from app import db
from app.models import User


auth_blueprint = Blueprint('auth_blueprint', __name__)


class RegistrationView(MethodView):
    def post(self):
        data = request.get_json(force=True)
        print("print data")
        print(data['password'])
        print(data['email'])
        user = User.query.filter_by(email=data['email']).first()
        if not user:
            try:
                email = data['email']
                password = data['password']
                user = User(email=email, password=password)
                user.save()
                response = {
                    'message': 'You registered successfully. Please log in.'
                }
                return make_response(jsonify(response)), 201
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 401
        else:
            response = {
                'message': 'User already exists. Please login.'
            }
            return make_response(jsonify(response)), 202


class LoginView(MethodView):
    def post(self):
        data = request.get_json(force=True)
        email = data['email']
        password = data['password']
        try:
            user = User.query.filter_by(email=email).first()
            if user and user.password_is_valid(password):
                access_token = user.generate_token(user.id)
                if access_token:
                    response = {
                        "message": "you logged in successfully",
                        'access_token': access_token.decode()
                    }
                    return make_response(jsonify(response)), 200
                else:
                    response = {
                        'message': 'Invalid email or password, Please try again'
                    }
                    return make_response(jsonify(response)), 401

        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500


registration_view = RegistrationView.as_view('registration_view')
login_view = LoginView.as_view('login_view')


auth_blueprint.add_url_rule(
    '/auth/register', view_func=registration_view, methods=['POST'])

auth_blueprint.add_url_rule(
    '/auth/login', view_func=login_view, methods=['POST'])


"""
{
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjR9.Xvj-KqqSVl_VB2w4vkx2ENiMx_2Sk4Sc8XkkyV0cJKE",
	"message": "you logged in successfully"
}
"""
