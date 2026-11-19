from datetime import datetime, timezone, timedelta
import jwt
from app.core.config import setting

def create_access_token(user_id: int) -> str:
    # token expires
    expires_at = (
        datetime.now(timezone.utc) + timedelta(minutes= setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    # create payload
    payload = {
        "sub" : user_id,
        "exp" : expires_at
    }
    
    return jwt.encode(
        payload,
        setting.SECRET_KEY,
        algorithm=setting.ALGORITHM
    )
    

def verify_access_tokens(token : str) -> dict:
    try:
        payload = jwt.decode(
            token,
            setting.SECRET_KEY,
            algorithms=setting.ALGORITHM
        )
        
        return payload
    except jwt.InvalidTokenError:
        return None
        
    
