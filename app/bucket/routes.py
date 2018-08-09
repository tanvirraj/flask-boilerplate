from flask import jsonify, request, Blueprint, json
from app import db
from app.models import Bucketlist


bucketlist = Blueprint('bucketlist', __name__)


@bucketlist.route('/')
@bucketlist.route('/bucketlists', methods=['GET', 'POST'])
def bucket():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print('name==')
        name = data['name']
        print(name)
        if name:
            bucketlist = Bucketlist(name=name)
            db.session.add(bucketlist)
            db.session.commit()
            response = jsonify({
                'id': bucketlist.id,
                'name': bucketlist.name,
                'date_created': bucketlist.date_created,
                'date_modified': bucketlist.date_modified
            })
            response.status_code = 200
            return response
    else:
        bucketlists = Bucketlist.query.all()
        results = []
        for bucket in bucketlists:
            obj = {
                'id': bucket.id,
                'name': bucket.name,
                'date_created': bucket.date_created,
                'date_modified': bucket.date_modified

            }
            results.append(obj)

        print("resutl")
        print(results)
        response = jsonify(results)
        response.status_code = 200
        return response


@bucketlist.route("/bucketlists/<int:bucket_id>", methods=['GET', 'PUT', 'DELETE'])
def get_single_bucket(bucket_id):
    bucket = Bucketlist.query.filter_by(id=bucket_id).first()
    if request.method == 'DELETE':
        db.session.delete(bucket)
        db.session.commit()
        response = jsonify({
            "message": "your bucket is just deleted. sorry"
        })
        response.status_code = 200
        return response
    elif request.method == 'PUT':
        bucket.name = request.json['name']
        db.session.add(bucket)
        db.session.commit()
        response = jsonify({
            'id': bucket.id,
            'name': bucket.name,
            'date_created': bucket.date_created,
            'date_modified': bucket.date_modified
        })
        response.status_code = 200
        return response
    else:
        response = jsonify({
            'id': bucket.id,
            'name': bucket.name,
            'date_created': bucket.date_created,
            'date_modified': bucket.date_modified
        })
        response.status_code = 200
        return response
