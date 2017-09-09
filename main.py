from flask import Flask, jsonify

from models import get_user

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<username>", methods=['GET'])
def view_status(username):
    user = get_user()
    return jsonify(user.to_json())

@app.route("/user/<username>", methods=["PUT"])
def update_status(username):
    user = get_user()
    # TODO save to database
    pass
