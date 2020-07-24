from flask import Flask, abort, jsonify, abort
from flask_cors import CORS

from models import Project, Student, setup_db
from auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)

CORS(app)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, PATCH, OPTIONS')
    return response

@app.route('/')
def healty():
    return "Healthy"