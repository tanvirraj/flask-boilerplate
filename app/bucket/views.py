from flask import jsonify, request, Blueprint, json, make_response
from app import db
from app.models import Bucketlist, User


bucketlist = Blueprint('bucketlist', __name__)


@bucketlist.route('/')
@bucketlist.route('/bucketlists', methods=['GET', 'POST'])
def bucket():
    access_token = request.headers.get('Authorization')
    if access_token:
        user_id = User.decode_token(access_token)
        if isinstance(user_id, int):
            if request.method == "POST":
                data = request.get_json(force=True)
                name = data['name']
                if name:
                    bucketlist = Bucketlist(name=name, created_by=user_id)
                    bucketlist.save()
                    response = jsonify({
                        'id': bucketlist.id,
                        'name': bucketlist.name,
                        'date_created': bucketlist.date_created,
                        'date_modified': bucketlist.date_modified,
                        'created_by': user_id
                    })

                    return make_response(response), 201

            else:
                bucketlists = Bucketlist.query.filter_by(created_by=user_id)
                results = []

                for bucketlist in bucketlists:
                    obj = {
                        'id': bucketlist.id,
                        'name': bucketlist.name,
                        'date_created': bucketlist.date_created,
                        'date_modified': bucketlist.date_modified,
                        'created_by': bucketlist.created_by
                    }
                    results.append(obj)

                return make_response(jsonify(results)), 200
        else:
            message = user_id
            response = {
                'message': message
            }
            return make_response(jsonify(response)), 401


@bucketlist.route("/bucketlists/<int:bucket_id>", methods=['GET', 'PUT', 'DELETE'])
def get_single_bucket(bucket_id):
    access_token = request.headers.get('Authorization')
    if access_token:
        user_id = User.decode_token(access_token)
        if isinstance(user_id, int):
            bucket = Bucketlist.query.filter_by(id=bucket_id).first()
            if request.method == 'DELETE':
                db.session.delete(bucket)
                db.session.commit()
                response = {
                    "message": "bucketlist {} deleted".format(bucket.id)
                }
                return make_response(jsonify(response)), 200
            elif request.method == 'PUT':
                data = request.get_json(force=True)
                bucket.name = data['name']
                db.session.add(bucket)
                db.session.commit()
                response = jsonify({
                    'id': bucket.id,
                    'name': bucket.name,
                    'date_created': bucket.date_created,
                    'date_modified': bucket.date_modified,
                    'created_by': bucket.created_by
                })
                return make_response(response), 200
            else:
                response = jsonify({
                    'id': bucket.id,
                    'name': bucket.name,
                    'date_created': bucket.date_created,
                    'date_modified': bucket.date_modified,
                    'created_by': bucket.created_by
                })
                return make_response(response), 200
        else:
            message = user_id
            response = {
                'message': message
            }
            return make_response(jsonify(response)), 401
