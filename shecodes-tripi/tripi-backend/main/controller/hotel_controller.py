from flask import request, jsonify, make_response, Blueprint, render_template

from main.service.user_service import UserService
from main.service.hotel_service import HotelService
from main.errors import NotFoundError

api = Blueprint('hotel_api', __name__, template_folder='templates')
hotel_service = HotelService()


@api.route("/hotels/autocomplete")
def get_autocomplete():
    try:
        return make_response(jsonify({
            'status-code': 200,
            'message': 'Success',
            'data': hotel_service.get_autocomplete(**request.args),
        }), 200)
    except NotFoundError as e:
        return make_response(jsonify({
            'message': e.message,
            'status-code': 400
        }), 400)
    except TypeError as e:
        return make_response(jsonify({
            'message': str(e),
            'status-code': 403
        }), 403)
    except Exception as e:
        print(e)
        return make_response(jsonify({
            'message': 'An unexpected error has occured',
            'status-code': 500
        }), 500)


@api.route("/hotels/search")
def get_hotels():
    try:
        return make_response(jsonify({
            'message': 'Success',
            'status-code': 200,
            'data': hotel_service.search_hotels(**request.args)
        }), 200)
    except NotFoundError as e:
        return make_response(jsonify({
            'message': e.message,
            'status-code': 400
        }), 400)
    except TypeError as e:
        return make_response(jsonify({
            'message': str(e),
            'status-code': 403
        }), 403)
    except Exception as e:
        print(e)
        return make_response(jsonify({
            'message': 'An unexpected error has occured',
            'status-code': 500
        }), 500)


@api.route("/hotels/recommendation/<string:recommendation_type>")
def get_hotel_recommendation(recommendation_type):
    try:
        return make_response(jsonify({
            'message': 'Success',
            'status-code': 200,
            'data': hotel_service.get_recommendation(recommendation_type, **request.args)
        }), 200)
    except NotFoundError as e:
        return make_response(jsonify({
            'message': e.message,
            'status-code': 400
        }), 400)
    except TypeError as e:
        return make_response(jsonify({
            'message': str(e),
            'status-code': 403
        }), 403)
    except Exception as e:
        print(e)
        return make_response(jsonify({
            'message': 'An unexpected error has occured',
            'status-code': 500
        }), 500)


# @api.route("/hotels/getprice")
# def get_hotel_price():
#     hotel_id = request.args['hotel-id'].lower()
#     price = hotel_service.get_hotel_score(hotel_id)
#     return make_response(jsonify({
#         'message': 'Success',
#         'status-code': 200,
#         'data': price
#     }), 200)
