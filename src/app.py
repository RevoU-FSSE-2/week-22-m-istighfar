import os
from flask import Flask
from redis import Redis
from config import Config
from extensions import mail, limiter, redis_client
from db import db, db_init
from common.bcrypt import bcrypt
from auth.apis import auth_blp
from user.apis import user_blueprint
from task.apis import task_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_talisman import Talisman


app = Flask(__name__)
app.config.from_object(Config)

allowed_origins = ["http://localhost:5173", "https://clinquant-nougat-f52198.netlify.app"]
CORS(app, resources={r"/*": {"origins": allowed_origins}})

Talisman(app, content_security_policy={
    'default-src': '\'self\'',
    'img-src': ['\'self\'', 'data:'],
    'script-src': ['\'self\'', '\'unsafe-inline\''],
    'connect-src': ['\'self\'', 'http://127.0.0.1:5000']
})




redis_client = Redis(host='localhost', port=6379, db=0)

db.init_app(app)
bcrypt.init_app(app)
mail.init_app(app)
limiter.init_app(app)

SWAGGER_URL = '/swagger'  
API_URL = '/static/swagger.yaml'  

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={  
        'app_name': "Task Geass APIs"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(auth_blp, url_prefix="/auth")
app.register_blueprint(task_blueprint, url_prefix="/user")
app.register_blueprint(user_blueprint, url_prefix="/admin")

# with app.app_context():
#     db_init()
