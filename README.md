# Udacious
Online Project hub for udacity students

Udacious is an online hub for udacity students to share their projects, get feedback and connect with other students.
This documentation is for the backend api of the project which is hosted here - https://udacious.herokuapp.com/ The project has it's frontend hosted at http://udacious-frontend.herokuapp.com/ . It should be noted that the frontend app is yet to implement all the functionality this backend api is capable of.

## Getting Started

- Base URL: https://udacious.herokuapp.com/
- API Keys: None used

## RBAC controls
This project has primarily two roles
- Student
    Permission: none
- Admin
    Permissions: `delete:projects` and  `delete:student`


### Valid token for sample student - 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR6VjNiNG1jcFZXODJfWDhvbkhOWSJ9.eyJpc3MiOiJodHRwczovL2VsaWphaGRldi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxYjM5NWNlNmEyOTEwMDM3Mjc2Nzk4IiwiYXVkIjoidWRhY2lvdXMiLCJpYXQiOjE1OTU4NjY2MTAsImV4cCI6MTU5NTk1MzAxMCwiYXpwIjoiWm5Ocno0a2U1TTFLYU9pZ2xDZ01xWkRYR0pQcU51Tk0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.E96Wc68V9DbYQYSjgbT35rSr6a11dRSBY2zGfFw1V-FmuRMdfw9rKvf2cREu6xWCm0pVB59GJlFTzNd9CSNT5gtGDz49aSjtBgNewmsEFc2mA9UdSOZjNIkIQrLWYC0HY6JrbAad8pr0Seifwm7sHGqIbevauFtkjQlfPGs1ntIc7LGFh504tNaUA06_Ax0GThfjp4Sk-uFPkUbrq_MAkZvO1RdNIMemoA8AomqatifgFwOtqYNuSAF2qBREFnETPLKBaKJfGdQc1LYfNaXBqCesPvyQJLecDL2boU7jLIml2sZBYiImRTXu3sw6-KnZzObZCmILtLr1m9O-A9lQBw

**Note**: New tokens can be gotten from https://elijahdev.us.auth0.com/authorize?audience=udacious&response_type=token&client_id=ZnNrz4ke5M1KaOiglCgMqZDXGJPqNuNM&redirect_uri=http://localhost:5000/ after signup

### Valid token for sample admin
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlR6VjNiNG1jcFZXODJfWDhvbkhOWSJ9.eyJpc3MiOiJodHRwczovL2VsaWphaGRldi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxMWQ2YTZkYmY2ZmYwMDEzNWM3N2I1IiwiYXVkIjoidWRhY2lvdXMiLCJpYXQiOjE1OTU4NzQ1OTIsImV4cCI6MTU5NTk2MDk5MiwiYXpwIjoiWm5Ocno0a2U1TTFLYU9pZ2xDZ01xWkRYR0pQcU51Tk0iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9qZWN0IiwiZGVsZXRlOnN0dWRlbnQiXX0.kLqRU42QBKguX6EXU7BM37b8o9KmTFPXvc8cRwVK0o-sl1drIZ8cqAjc_8mr7SH9jvDqZXG9SwLlTidG9b1Zhqrca8bA48yyCWq06dkwwqEi37Q4beRyKW_RgmlC0vqQxvD29aej05z4DbiMEzKFyt8CLD0GuilL41CPGuzztV8GZN7GIsqEKSmRi36reg3Niiasv6ZCSk7wPWRPm-dmI8_xgnXK2RMyscRnjekpyasdvHS_MjwaFeCQjyVCqDqsdOSYwWHfV1MXtTMYMGAprWVCyrNSJL0al_mqhsHYnoej1X0OSRiq85xAgAiKIv5sYH8vk118U1GefHXVWlJcaQ

**Note**: You can contact the author (see details below) for new admin tokens


## API Endpoints

GET '/projects'
GET '/projects/<int:id>'
POST '/projects'
PATCH '/projects/<int:id>'
DELETE '/projects/<int:id>'
DELETE '/students/<int:id>'
POST '/projects/<int:id>/comments'

### Endpoints Behaviour
GET '/projects'
- Fetches a list of all projects posted by students
- Request arguments: None
- Returns: An object with containing a list of projects and detailed descriptions on it.


GET '/projects/<int:id>'
- Fetches a project and details about it
- Parameters: id (integer)
	id:  Specifies the id of the project
- Headers required: 'Content-Type', 'Authorization" with 'bearer {{token}}' as value
- Returns: An object containing the details of the project with id specified


POST '/projects'
- Post a project into the database
- Requies authentication
- No permissions required (only autehtication not authorization)
- The comment author is added to the students table if the author doesn't exits
- Headers required: 'Content-Type', 'Authorization" with 'bearer {{token}}' as value
```
Request Body: {
    "name": "Test app",
    "description": "Super interesting content",
    "project_duration": 10,
    "notes": "Some content here",
    "image_url": "https://unsplash.com" 
}
```
- Returns: An oject containing a success property of 'True' and the new project's id


PATCH '/projects/<int:id>'
- To change the details of a project
- **ONLY** the author of the project can do this.
- Parameters: id (integer)
	id:  Specifies the id of the project
- Headers required: 'Content-Type', 'Authorization" with 'bearer {{token}}' as value
- Request Body : {
    "name": "New project name", 
    "description": "New description",
    "project_duration": 10,
    "notes": "New note............",
    "image_url": "https://new_image_url.ext" 
}
 	

DELETE '/projects/<int:id>'
- To delete a project
- **ONLY** the admins can do this.
- Parameters: id (integer)
	id:  Specifies the id of the project
- Request body: None
- Returns: An oject containing a success property of 'True' and the deleted project's id


DELETE '/students/<int:id>'
- To delete a project
- This also deletes all project associted with the given student
- **ONLY** the admins can do this.
- Parameters: id (integer)
	id:  Specifies the id of the project
- Request body: None
- Returns: An oject containing a success property of 'True' and the deleted student's id


POST '/projects/<int:id>/comments'
- To post a comment on a project
- Requies authentication
- No permissions required (only autehtication not authorization)
- The comment author is added to the students table if the author doesn't exits
- Headers required: 'Content-Type', 'Authorization" with 'bearer {{token}}' as value
```
Request body: {
    "comment": "I like your project. You've done quite a lot of work"
}
```
- Returns: An oject containing a success property of 'True' and the new comment's details


## Error types

- 404 : Resource not found

```
Sample Result : {
  "message": "Resource Not Found",
  "success": false
}
```

- 405 : Method not allowed - you should check you query method and the endpoint

```
Sample Result : {
  "message": "Method not allowed",
  "success": false
}
```

- 400 : Bad Request - you should check the body of your request for errors

```
Sample Result : {
  "message": "Method not allowed",
  "success": false
}
```

- 422 : Unprocessable - request valid but server can process it for some reason

```
Sample Result : {
  "message": "Unprocessable",
  "success": false
}
```

- 500 : [RARE] Something went wrong in the server while trying to execute the request

```
Sample Result : {
  "message": "Unprocessable",
  "success": false
}
```
## Author
- Kolawole Elijah Semilogo.
- Email: elijahkolawole1@gmail.com


## Acknowledgments:
With the help of this people and organizations, this project has been made possible 

- Udacity for their great content and valuable education
- Heroku for their free hosting service for learners and hobyists like myself
- My elder sister Kolawole Ayinoluwa Ewatomi for her love and support (whose smooth wifi connection made this project a reality). Thank you so much.
- My parents Paul and Favour. They always push me to do the best I can.


## Notes
- This backend api repository is hosted on github here - https://github.com/prof2k/udacious
- The frontend repository which consumes this api is hosted on github here - https://github.com/prof2k/udacious-frontend

