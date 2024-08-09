# Flask-REST-API

Creating a REST API using the *Test-First* methodology with the below specified endpoints (expected API requests). Data format will be [JSON](http://www.json.org/) only for now.
JSON : a dictionary of key,value text pairs
*Test-First* helps us creating a better API and should make software development a bit more efficient. I think it helps us create the right thing.

# REST API
Is a way of thinking about how a web server responds to requests
It reponds with resources, not just data
The server has access to resources and each resource is interacted with by means of a request.
REST is stateless - each request is independent of any other requests. 
Example logged in user - this data has to be send with every request 

## HTTP verbs ##
**GET /items**
Return a list of items in JSON format.
Ex. {"name": "chair", "price": "15.99", "currency": "$"}

**GET /item/<name>**
Return a single item with the given name. Return format is JSON. Item names are unique.

**POST /item/<name>**
Create an item with the given name. If the item already exists, the action fails.

**DEL /item/<name>**
Delete the item with the given name.

**PUT /item/<name>**
Update the item with the given name. If it doesn't exist yet, create it.

Looking at these endpoints, we'll see 2 resources, ie ++items++ and ++item++.

# Tools used (added as needed)
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
Postman for API testing (getpostman.com)

# Start application
python3 app.py

# Misc
Difference between models and resources:
    Resources are an external representation (users interact with it)
    Models are an internal representation of resources