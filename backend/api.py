from flask import Flask, abort, jsonify, abort, request
from flask_cors import CORS

from models import Project, Student, setup_db
from auth import AuthError, requires_auth
import sys

app = Flask(__name__)
setup_db(app)

CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, DELETE, PATCH, OPTIONS')
    return response


@app.route('/')
def healthy():
    return 'Healthy'

# To get all projects


@app.route('/projects', methods=['GET'])
def get_projects():
    try:
        projects = Project.query.all()
        formated_projects = [project.format for project in projects]
    except:
        print(sys.exec_info())
        abort(500)
    return jsonify({
        'success': 200,
        'projects': formated_projects
    }), 200

# To post a project


@app.route('/projects', methods=['POST'])
@requires_auth('')
def add_project(payload):
    data = request.get_json()
    try:
        if data:
            new_project = Project(
                name = data['name'],
                description = data['description'],
                project_duration_in_days = data['project_duration'],
                notes = data['notes'],
                image_url = data['image_url'],
                # student_id = payload['sub']
            )
            new_project.insert()
        else:
            abort(400)
    except:
        print(sys.exc_info())
        abort(422)
    return jsonify({
        'success': True,
        'project_id': new_project.id
    }), 200



@app.route('/login')
def login(payload):
    return 'hello world'


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': 'Resource Not Found'
    }), 404



@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'success': False,
        'message': 'Bad Request'
    }), 400


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        'success': False,
        'message': 'Unprocessable'
    }), 422


@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'success': False,
        'message': 'Internal Server Error'
    }), 500
