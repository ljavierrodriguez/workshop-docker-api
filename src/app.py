import os
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
from models import db, User

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = os.getenv('DEBUG')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/')
def main():
    return jsonify({
        "status": "Server running successfully"
    }), 200

@app.route('/api/users')
def list_users():

    users = User.query.all()
    users = [user.username for user in users]

    return jsonify({
        "users": users
    }), 200

@app.route('/api/users', methods=['POST'])
def add_user():

    username = request.json.get('username')

    if not username:
        return jsonify({ "message": "Username is required"}), 422
    
    found = User.query.filter_by(username=username).first()

    if found:
        return jsonify({ "message": "User already exists"}), 422
    
    user = User()
    user.username = username

    db.session.add(user)
    db.session.commit()

    return jsonify({ "status": "success", "message": "User created successfully"}), 201

if __name__ == '__main__':
    app.run()