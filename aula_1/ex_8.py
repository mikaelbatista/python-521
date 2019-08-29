
import sys
import os
import bson

import flask
import pymongo


#################################################
# Models
#################################################

client = pymongo.MongoClient()
db = client.picolo

class User:

    @staticmethod
    def find_all(params):
        return [ 
            User(**u) for u in db.users.find(params)
        ]

    @staticmethod
    def find(params):
        u = db.users.find_one(params)
        if u:
            return User(**u)
        return None

    def __init__(self, name, email, age, password, **kwargs):
        self.name = name
        self.email = email
        self.age = int(age)
        self.password = password 
        self._id = kwargs.get('_id')
    
    @property
    def primary_key(self):
        return {
            'email': self.email
        }
    
    @property
    def to_json(self):
        return {
            'id': str(self._id) if self._id is not None else None,
            'name': self.name,
            'email': self.email,
            'age': self.age
        }
    
    def authenticate(self, password):
        pass
    
    def delete(self):
        db.users.remove(self.primary_key)

    def save(self):
        db.users.update_one(self.primary_key, {
            '$set': {
                'name': self.name,
                'email': self.email,
                'age': self.age,
                'password': self.password
            }
        }, upsert=True)

#################################################
# Application
#################################################

app = flask.Flask(__name__)

@app.route('/')
def get_index():
    return 'vai corinthians'

@app.route('/users', methods=[ 'GET' ])
def get_users():
    return flask.jsonify([
        u.to_json for u in User.find_all({})
    ])

@app.route('/users', methods=[ 'POST' ]) 
def post_users():

    form = flask.request.json

    required_attributes = [ 'name', 'email', 'age', 'password' ]

    for attribute in required_attributes:
        if attribute not in form:
            return flask.jsonify({
                'message': '{} required'.format(attribute)
            }), 400

    user = User.find({
        'email': form.get('email')
    })

    if user:
        return flask.jsonify({
            'message': 'user already exists'
        }), 400
    
    user = User(**form)
    user.save()

    return flask.jsonify({
        'message': 'user created'
    }), 201

@app.route('/users/<user_id>', methods=[ 'GET' ])
def get_users_by_id(user_id):

    user = User.find({ 
        '_id': bson.ObjectId(user_id)
    })

    if not user:
        return flask.jsonify({
            'message': 'user not found'
        }), 404

    return flask.jsonify(user.to_json), 200 

@app.route('/users/<user_id>', methods=[ 'PUT' ])
def put_users_by_id(user_id):
    
    user = User.find({ 
        '_id': bson.ObjectId(user_id)
    })

    if not user:
        return flask.jsonify({
            'message': 'user not found'
        }), 404
    
    form = flask.request.json

    for key, value in form.items():
        setattr(user, key, value)
    
    user.save()

    return flask.jsonify({
        'message': 'user updated'
    }), 200

@app.route('/users/<user_id>', methods=[ 'DELETE' ])
def delete_users_by_id(user_id):

    user = User.find({ 
        '_id': bson.ObjectId(user_id)
    })

    if not user:
        return flask.jsonify({
            'message': 'user not found'
        }), 404
    
    user.delete()

    return flask.jsonify({
        'message': 'user deleted'
    }), 200

if __name__ == '__main__':

    current_module = os.path.abspath(os.path.curdir)
    sys.path.append(current_module)

    os.environ['FLASK_ENV'] = 'development'
    os.environ['FLASK_APP'] = 'ex_8.py'

    app.run(host='0.0.0.0', debug=True)