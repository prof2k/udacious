import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Project, Student, Comment, db

student_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR6VjNiNG1jcFZXODJfWDhvbkhOWSJ9.eyJpc3MiOiJodHRwczovL2VsaWphaGRldi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxYjM5NWNlNmEyOTEwMDM3Mjc2Nzk4IiwiYXVkIjoidWRhY2lvdXMiLCJpYXQiOjE1OTU4NjY2MTAsImV4cCI6MTU5NTk1MzAxMCwiYXpwIjoiWm5Ocno0a2U1TTFLYU9pZ2xDZ01xWkRYR0pQcU51Tk0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.E96Wc68V9DbYQYSjgbT35rSr6a11dRSBY2zGfFw1V-FmuRMdfw9rKvf2cREu6xWCm0pVB59GJlFTzNd9CSNT5gtGDz49aSjtBgNewmsEFc2mA9UdSOZjNIkIQrLWYC0HY6JrbAad8pr0Seifwm7sHGqIbevauFtkjQlfPGs1ntIc7LGFh504tNaUA06_Ax0GThfjp4Sk-uFPkUbrq_MAkZvO1RdNIMemoA8AomqatifgFwOtqYNuSAF2qBREFnETPLKBaKJfGdQc1LYfNaXBqCesPvyQJLecDL2boU7jLIml2sZBYiImRTXu3sw6-KnZzObZCmILtLr1m9O-A9lQBw"
admin_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR6VjNiNG1jcFZXODJfWDhvbkhOWSJ9.eyJpc3MiOiJodHRwczovL2VsaWphaGRldi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxMWQ2YTZkYmY2ZmYwMDEzNWM3N2I1IiwiYXVkIjoidWRhY2lvdXMiLCJpYXQiOjE1OTU4NzQ1OTIsImV4cCI6MTU5NTk2MDk5MiwiYXpwIjoiWm5Ocno0a2U1TTFLYU9pZ2xDZ01xWkRYR0pQcU51Tk0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9qZWN0IiwiZGVsZXRlOnN0dWRlbnQiXX0.kLqRU42QBKguX6EXU7BM37b8o9KmTFPXvc8cRwVK0o-sl1drIZ8cqAjc_8mr7SH9jvDqZXG9SwLlTidG9b1Zhqrca8bA48yyCWq06dkwwqEi37Q4beRyKW_RgmlC0vqQxvD29aej05z4DbiMEzKFyt8CLD0GuilL41CPGuzztV8GZN7GIsqEKSmRi36reg3Niiasv6ZCSk7wPWRPm-dmI8_xgnXK2RMyscRnjekpyasdvHS_MjwaFeCQjyVCqDqsdOSYwWHfV1MXtTMYMGAprWVCyrNSJL0al_mqhsHYnoej1X0OSRiq85xAgAiKIv5sYH8vk118U1GefHXVWlJcaQ"


class UdaciousTesting(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:password@localhost:5432/udacity_test"

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_app_working(self):
        res = self.app.get('/')
        data = res.json

        self.assertTrue(res.status_code, 200)

    def test_projects(self):
        res = self.app.get('/projects')
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['projects'])

    def test_get_project(self):
        res = self.app.get('/projects/1')
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['projects']))

    def test_404_projects(self):
        res = self.app.get('/projects/1000')
        data = res.json

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_add_project(self):
        body = {
            "name": "Test app",
            "description": "Super interesting content",
            "project_duration": 10,
            "notes": "Blah blah blah......>",
            "image_url": "https://unsplash.com" 
        }

        res = self.app.post('/projects', 
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer '+ student_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_add_project(self):
        body = {
            "name": "Test app",
            "description": "Super interesting content",
            "project_duration": 10,
            "notes": "Blah blah blah......>",
            "image_url": "https://unsplash.com" 
        }

        res = self.app.post('/projects', 
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer definitely_not_a_token'
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 401)

    def test_update_project(self):
        body = {
            "description": "Trello Clone",
            "image_url": "https://google.com", 
            "name": "Quicker than fire", 
            "notes": "some interesting text",
            "project_duration": 4
        }

        res = self.app.patch('/projects/1', 
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer '+ student_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_401_update_project(self):
        body = {
            "description": "Trello Clone",
            "image_url": "https://google.com", 
            "name": "Quicker than fire", 
            "notes": "some interesting text",
            "project_duration": 4
        }

        res = self.app.patch('/projects/1', 
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer definitely_not_a_token'
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 401)

    def test_404_update_project(self):
        body = {
            "description": "Trello Clone",
            "image_url": "https://google.com", 
            "name": "Quicker than fire", 
            "notes": "some interesting text",
            "project_duration": 4
        }

        res = self.app.patch('/projects/1000', 
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer '+ student_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_project(self):
        res = self.app.get('/projects/1')
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['projects']))

    def test_404_projects(self):
        res = self.app.get('/projects/1000')
        data = res.json

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)


    # Delete Project tests
    def test_delete_project(self):
        res = self.app.delete('/projects/1', 
                headers= {
                    'Authorization': 'bearer '+ admin_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['project_id'])

    def test_401_delete_project(self):
        res = self.app.delete('/projects/2', 
                headers= {
                    'Authorization': 'bearer definitely_not_a_token'
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 401)

    def test_404_delete_project(self):
        res = self.app.delete('/projects/1000', 
                headers= {
                    'Authorization': 'bearer '+ admin_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 404)

    # Delete Student Test
    # def test_delete_student(self):
    #     res = self.app.delete('/students/2', 
    #             headers= {
    #                 'Authorization': 'bearer '+ admin_token
    #             }
    #         )
    #     data = res.json

    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['student_id'])

    def test_401_delete_student(self):
        res = self.app.delete('/students/1', 
                headers= {
                    'Authorization': 'bearer definitely_not_a_token'
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 401)

    def test_404_delete_student(self):
        res = self.app.delete('/students/1000', 
                headers= {
                    'Authorization': 'bearer '+ admin_token
                }
            )
        data = res.json

        self.assertEqual(res.status_code, 404)

    # Add comment test
    def test_add_comment(self):
        body = {
            "comment": "I like your project. You've done quite a lot of work"
        }
        res = self.app.post('/projects/3/comments',
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer '+ Addmin_token
                })
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['comment'])

    def test_401_add_comment(self):
        body = {
            "comment": "I like your project. You've done quite a lot of work"
        }
        res = self.app.post('/projects/3/comments',
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer definitely_not_a_token'
                })

        data = res.json

        self.assertEqual(res.status_code, 401)

    def test_404_add_comment(self):
        body = {
            "comment": "I like your project. You've done quite a lot of work"
        }
        res = self.app.post('/projects/1000/comments',
                data=json.dumps(body),
                headers= {
                    'Content-Type': 'application/json',
                    'Authorization': 'bearer '+ admin_token
                })
        data = res.json

        self.assertEqual(res.status_code, 404)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
