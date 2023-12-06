

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

- [Task Geass App](https://clinquant-nougat-f52198.netlify.app) - Frontend application.
- [Swagger API Documentation](http://34.126.184.177/swagger/) - Backend API documentation.
- [Postman API Documentation](https://documenter.getpostman.com/view/28996754/2s9YeK3pdX) - Postman collection for API testing.

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
5. Set up environment variables:**
   - Copy `.env.example` to a new file named `.env` in the `src` directory.
   - Modify the `.env` file with your specific configurations.

5. Start the Flask development server:
   ```
   flask run
   ```
6. Open your browser and navigate to `http://localhost:5000` or the port you set.


## Tech Stack
- **Frontend**: React, React Router DOM, Ant Design, Vite, TypeScript, Moment.js, vite-plugin-pwa.
- **Backend**: Flask, various Flask extensions, SQLAlchemy, Redis, Psycopg2-binary, PyJWT, Marshmallow, Faker, Gunicorn.
- **Database**: PostgreSQL.
- **DevOps**: Docker, Google Cloud Platform.

## API Endpoint

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
