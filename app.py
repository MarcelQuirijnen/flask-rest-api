from flask import Flask
from flask_restful import Api
# JSON web token
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# Turns off the flask mod tracker since sqlalchemy has its own version now
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'sh1n0b1'  # should not be visible in production

api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# JWT creates a new endpoint /auth
# when /auth is requested, we send it a username and password and JWT forwards it to authenticate.
# authenticate returns a user object, which is converted to a JWT token
# that token is send to the next middleware method, which is identity
# identity turns this into the correct user_id
jwt = JWT(app, authenticate, identity)  # implemented in security.py

# map endpoints to resources/classes
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    # only do this if we run the app
    from db import db
    db.init_app(app)

    app.run(port=5000)
