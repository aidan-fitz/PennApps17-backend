from flask import Flask, jsonify

from models import get_user, User
from database import db_session

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<username>", methods=['GET'])
def view_status(username):
    user = get_user(username)
    return jsonify(user.to_json())

@app.route("/user/<username>", methods=["PUT"])
def update_status(username):
    # Get user from db model
    user = get_user(username)

    # Parse request body as JSON
    json_in = request.json

    # Copy fields from JSON object to model
    user.from_json(json_in)

    # Save to database
    user.save()
    db_session.commit()

@app.route("/user/", methods=["POST"])
def new_user():
    json = request.json
    user = User(json)
    db_session.add(user)
    db_session.commit()

