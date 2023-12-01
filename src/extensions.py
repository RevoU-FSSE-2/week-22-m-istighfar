from flask_mail import Mail
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

redis_url = "redis://default:P1C1fnA4ePBLpeLogLGdfbIfoDc5CeP6@viaduct.proxy.rlwy.net:32232"
redis_client = Redis.from_url(redis_url)

mail = Mail()
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)
