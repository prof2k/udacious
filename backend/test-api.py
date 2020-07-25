import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Project, Student, db


class UdaciousTesting(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:password@localhost:5432/udacious_test"
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

# self.app = app
# self.client = self.app.test_client
# self.database_name = "udacity_test"
# self.database_path = f"postgresql://postgres:password@localhost:5432/{self.database_name}"
# setup_db(self.app)

# # binds the app to the current context
# with self.app.app_context():
#     self.db = SQLAlchemy()
#     self.db.init_app(self.app)
#     # create all tables
#     self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_app_working(self):
        res = self.client.get('/')
        data = res.json

        self.assertTrue(res.status_code, 200)
        self.assertTrue(len(data))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
