from flask import Flask, abort, jsonify, abort, request
from flask_cors import CORS
from sqlalchemy import desc

from models import Project, Student, setup_db
from auth import AuthError, requires_auth
import sys
from datetime import datetime

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
    projects = Project.query.order_by(desc(Project.id)).all()

    # Check if there are any projects in the database
    if projects:
        try:
            formated_projects = [project.short() for project in projects]
        except:
            print(sys.exc_info())
            abort(422)
    else:
        formated_projects = []
    return jsonify({
        'success': 200,
        'projects': formated_projects
    }), 200 

# To get a project
@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get(id)
    if not project:
        abort(404)
    return jsonify({
        'success': 200,
        'projects': project.long()
    }), 200 

# (Only used aftter authorizing)
# Gets a student from the database or adds one if that student doesn't exist
def get_or_add_student(id):
    try:
        student = Student.query.filter_by(auth_id = id).one_or_none()

        if not student:
            student = Student(
                auth_id = id
            )
            student.insert()
    except:
        abort(422)
    return student

# To post a project
@app.route('/projects', methods=['POST'])
@requires_auth('')
def add_project(payload):
    data = request.get_json()
    student = get_or_add_student(payload['sub'])

    # Checks if the request body contains something
    if data: 
        try:    
            new_project = Project(
                name = data['name'],
                description = data['description'],
                project_duration_in_days = data['project_duration'],
                notes = data['notes'],
                image_url = data['image_url'],
                student_id = student.id
            )
            new_project.insert()
        except:
            print(sys.exc_info())
            abort(422)
    else:
        abort(400)
    return jsonify({
        'success': True,
        'project_id': new_project.id
    }), 200

# To update a project
@app.route('/projects/<int:id>', methods=['PATCH'])
@requires_auth()
def update_project(payload, id):
    project = Project.query.get(id)

    # Checks if such a project exists
    if project:
        project_author = Student.query.filter_by(id=project.student_id).one_or_none()

        # Checks if the editor is the author of the project
        if payload['sub'] == project_author.auth_id:
            data = request.get_json()
            print(data)
            try:
                project.name = data.get('name', project.name)
                project.description = data.get('description', project.description)
                project.project_duration_in_days = data.get('project_duration', project.project_duration_in_days)
                project.notes = data.get('notes', project.notes)
                project.image_url = data.get('image_url', project.image_url)
                project.update()
            except:
                print(sys.exc_info())
                abort(422)
        else:
            abort(403)
    else:
        abort(404)
    return jsonify({
        'success': True,
        'project': project.long()
    }), 200

# To delete a student and all corresponding projects (only Admins)
@app.route('/students/<int:id>', methods=['DELETE'])
@requires_auth('delete:student')
def delete_student(payload, id):
    student = Student.query.filter_by(id=id).one_or_none()

    # Checks if such a student exists
    if student:
        try:
            Project.query.filter(Project.student_id==id).delete()
            student.delete()
        except:
            print(sys.exc_info())
            abort(422)
    else:
        abort(404)
    return jsonify({
        'success': True,
        'student_id': student.id
    }), 200


# To delete a project (only Admins)
@app.route('/projects/<int:id>', methods=['DELETE'])
@requires_auth('delete:project')
def delete_project(payload, id):
    project = Project.query.filter_by(id=id).one_or_none()

    # Checks if such a project exists
    if project:
        try:
            project.delete()
        except:
            abort(422)
    else:
        abort(404)
    return jsonify({
        'success': True,
        'project_id': project.id
    }), 200
    
 
# Comments

# To add a comment
@app.route('/project/<int:id>/comments', methods=['POST'])
@requires_auth()
def add_comment(id, payload):
    data = request.get_json()
    
    # Checks if the body of the request contains anything
    if data:
        author = get_or_add_student(payload['sub'])
        try: 
            comment = Comment(
                time_stamp = datetime.now(),
                content = data['comment'],
                author_id = author.id 
            )
        except:
            abort(422)
    else:
        abort(400)
    return jsonify({
        'success': True
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
