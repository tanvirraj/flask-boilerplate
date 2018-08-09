# from app import db
# from flask import request, jsonify, json
# from app.models import Bucketlist


# @app.route('/')
# @app.route('/bucketlists', methods=['GET', 'POST'])
# def bucket():
#     if request.method == 'POST':
#         data = request.get_json(force=True)
#         print('name==')
#         name = data['name']
#         print(name)
#         if name:
#             bucketlist = Bucketlist(name=name)
#             db.session.add(bucketlist)
#             db.session.commit()
#             response = jsonify({
#                 'id': bucketlist.id,
#                 'name': bucketlist.name,
#                 'date_created': bucketlist.date_created,
#                 'date_modified': bucketlist.date_modified
#             })
#             response.status_code = 200
#             return response
#     else:
#         bucketlists = Bucketlist.query.all()
#         results = []
#         for bucket in bucketlists:
#             obj = {
#                 'id': bucket.id,
#                 'name': bucket.name,
#                 'date_created': bucket.date_created,
#                 'date_modified': bucket.date_modified

#             }
#             results.append(obj)

#         print("resutl")
#         print(results)
#         response = jsonify(results)
#         response.status_code = 200
#         return response


# @app.route('/bucketlist/<int:bucket_id>', methods=['GET'])
# def get_bucket_detail(bucket_id):
#     bucketlist = Bucketlist.query.filter_by(id=bucket_id).first()
#     print(bucketlist)
#     response = jsonify({
#         'id': bucketlist.id,
#         'name': bucketlist.name,
#         'date_created': bucketlist.date_created,
#         'date_modified': bucketlist.date_modified
#     })
#     response.status_code = 200

#     return response


# @app.route('/bucketlist/<int:bucket_id>', methods=['PUT'])
# def update_bucket_detail(bucket_id):
#     bucketlist = Bucketlist.query.filter_by(id=bucket_id).first()
#     bucketlist.name = request.json['name']
#     db.session.add(bucketlist)
#     db.session.commit()
#     response = jsonify({
#         'id': bucketlist.id,
#         'name': bucketlist.name,
#         'date_created': bucketlist.date_created,
#         'date_modified': bucketlist.date_modified
#     })
#     response.status_code = 200

#     return response


# @app.route('/bucketlist/<int:bucket_id>', methods=['DELETE'])
# def delete_bucket(bucket_id):
#     bucketlist = Bucketlist.query.filter_by(id=bucket_id).first()
#     db.session.delete(bucketlist)
#     db.session.commit()
#     response = jsonify({
#         "message": "your bucket is just deleted. sorry"
#     })
#     response.status_code = 200

#     return response
