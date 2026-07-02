from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings




def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire

    token = jwt.encode(to_encode, settings.SECRET, settings.ALGORITHM)
    
    return token