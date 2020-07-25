from flask_sqlalchemy import SQLAlchemy
import json


database_path = 'postgresql://postgres:password@localhost:5432/udacious'
db = SQLAlchemy()


# Basic setup of app and database
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

# To easily reset the databasse
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    project_duration_in_days = db.Column(db.Integer)
    notes = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)


    # To insert a new model into db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # To update an existing record in the db
    def update(self):
        db.session.commit()

    # To delete a model from the db
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def short(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'project_duration': self.project_duration_in_days,
            'student_id': self.student_id,
            'image_url': self.image_url
        }

    def long(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'project_duration': self.project_duration_in_days,
            'notes': self.notes,
            'student_id': self.student_id,
            'image_url': self.image_url
        }

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    auth_id = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String(100))
    db.relationship('Project', backref='author', lazy=True)

    # To insert a new model into db
    def insert(self):
        db.session.add(self)
        db.session.commit()

    # To update an existing record in the db
    def update(self):
        db.session.commit()

    # To delete a model from the db
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    