from flask import request, jsonify, make_response, Blueprint, render_template
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
from main.service.user_service import UserService
from main.model.revoked_token import RevokedTokenModel


api = Blueprint('user_api', __name__, template_folder='templates')


@api.route("/auth/login", methods=['Post'])
def login():
    # get the post data
    user_service = UserService()
    post_data = request.get_json()
    user_id = post_data.get('userId')
    try:
        user = user_service.Authenticate(user_id)
        if user is not None:
            print(user.name)
            access_token = create_access_token(identity=user.id)
            print(access_token)
            refresh_token = create_refresh_token(identity=user.id)
            print(refresh_token)
            response_object = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'data': user.name,
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return make_response(jsonify(response_object), 200)
        else:
            response_object = {
                'status': 'failed',
                'message': 'Unsuccessfully logged in, userId is not correct.',
            }
            return make_response(jsonify(response_object), 404)
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Try again'
        }
    return make_response(jsonify(response_object), 500)


@api.route("/auth/logout", methods=['Post'])
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    try:
        revoked_token = RevokedTokenModel(jti=jti)
        revoked_token.add()
        response_object = {
            'status': 'success',
            'message': 'user signed out successfully, access token has been revoked'
        }
        return make_response(jsonify(response_object), 200)
    except Exception as e:
        print(e)
        response_object = {
            'status': 'failed',
            'message': 'something went wrong'
        }
        return make_response(jsonify(response_object), 500)


@api.route("/auth/testingauthen", methods=['Get'])
@jwt_required
def get():
    return render_template('home.html')
