from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

redis_client = Redis(host='localhost', port=6379, db=0)
mail = Mail()
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)
