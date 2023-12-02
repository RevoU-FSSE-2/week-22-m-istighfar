

# Task Geass
A modern task management application designed to help you stay organized and productive.

<p align="left">    
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"  width="50" height="50" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" width="50" height="50" />         
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original-wordmark.svg" width="50" height="50" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" width="50" height="50" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original-wordmark.svg" width="50" height="50" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" width="50" height="50" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original-wordmark.svg" width="50" height="50" /> 
</p> 

## Live Deployment

The application is deployed live at: [Live URL](https://clinquant-nougat-f52198.netlify.app)
The API is available live at: [Swagger API Documentation](http://34.126.184.177/swagger/)
Postman is available at: [Postman API Documentation](https://documenter.getpostman.com/view/28996754/2s9YeK3pdX)

## Table of Contents

- [Task Geass](#task-geass)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Live Deployment](#live-deployment)
- [API Endpoint](#api-endpoint)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

## Key Features

- **User Authentication**: Safeguard your tasks and information with our user authentication system.
- **Enhanced Security with Login Rate Limiter**: Protect against brute-force attacks with a Redis-backed login rate limiter, ensuring secure access.
- **Login & Register**: Sign up to start organizing, or log in to access your tasks.
- **Secure Password Recovery**: Forget your password? Recover it securely.
- **Task Management**: Add, view, and edit tasks with ease.
- **Task Prioritization**: Determine which tasks need your attention first.
- **Mark Tasks as Complete**: Get the satisfaction of checking off completed tasks.
- **Sorting & Filtering**: Easily find and order your tasks.
- **Search**: Quickly locate specific tasks.

## Getting Started

### Prerequisites

Ensure you have the following software installed:
- **Python 3.11**: The programming language used.
- **Pipenv** (optional but recommended): A packaging tool for Python that simplifies dependency management.

### Installation

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/RevoU-FSSE-2/week-22-m-istighfar.git
   ```
2. Navigate to the cloned directory:
   ```
   cd week-22-m-istighfar
   ```
3. Install the required dependencies using Pipenv:
   ```
   pipenv install
   ```
4. Activate the virtual environment:
   ```
   pipenv shell
   ```
5. Start the Flask development server:
   ```
   flask run
   ```
6. Open your browser and navigate to `http://localhost:5000` or the port you set.


## Tech Stack

### Frontend:

- **React**: A JavaScript library for building user interfaces.
- **React Router DOM**: A collection of navigational components that compose declaratively with your app.
- **Ant Design**: A design system with values of Nature and Determinacy for better user experience of enterprise applications.
- **Vite**: An opinionated web dev build tool that serves your code via native ES modules.
- **TypeScript**: Superset of JavaScript that compiles to clean JavaScript output, adding optional static 
- **Moment.js**: Rich, comprehensive time & date utility library.
- **vite-plugin-pwa**: Vite plugin to add PWA capabilities to your project.

### Backend:

- **Flask**: A micro web framework written in Python.
- **Flask Extensions**: Various Flask extensions like Flask-SQLAlchemy, Flask-Bcrypt, Flask-Cors, Flask-Mail, Flask-Limiter, Flask-Talisman, Flask-SeaSurf, and Flask-Swagger-UI.
- **SQLAlchemy**: An ORM (Object-Relational Mapper) library for Python.
- **Redis**: An in-memory data structure store used as a database, cache, and message broker, particularly for implementing rate limiting in user authentication.
- **Psycopg2-binary**: A PostgreSQL adapter for Python.
- **PyJWT**: A Python library to work with JSON Web Tokens.
- **Marshmallow**: A library for complex data serialization and deserialization.
- **Faker**: A library for generating fake data.
- **Gunicorn**: A Python WSGI HTTP server for UNIX.

## API Endpoint

The API is available at: [API Endpoint](https://expensive-boa-pajamas.cyclic.app/api-docs)

| Method | Endpoint                          | Description                             |
|--------|-----------------------------------|-----------------------------------------|
| POST   | /auth/register                    | Register a new user                      |
| GET    | /auth/verify-email/{token}        | Verify user's email address             |
| POST   | /auth/login                       | Login user with redis rate limit                           |
| POST   | /auth/refreshToken                | Refresh the access token                 |
| POST   | /auth/request-password-reset      | Request a password reset email           |
| POST   | /auth/reset-password/{resetToken} | Reset user's password with a given token |
| GET    | /user/tasks                       | Get all tasks for the logged-in user     |
| POST   | /user/tasks                       | Create a new task for the logged-in user |
| DELETE | /user/tasks                       | Delete all tasks for the logged-in user  |
| GET    | /user/tasks/{id}                  | Get a specific task by ID                |
| PUT    | /user/tasks/{id}                  | Update a specific task by ID             |
| DELETE | /user/tasks/{id}                  | Delete a specific task by ID             |
| PATCH  | /user/tasks/{id}/complete         | Mark a specific task as complete         |
| GET    | /admin/list-user                  | Get a list of all users (Admin only)     |
| POST   | /admin/create-user                | Create a new user (Admin only)           |
| PUT    | /admin/update-user/{id}           | Update a specific user by ID (Admin only)|
| DELETE | /admin/delete-user/{id}           | Delete a specific user by ID (Admin only)|
