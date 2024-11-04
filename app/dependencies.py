from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from .config import SECRET_KEY, ALGORITHM
from .schemas import UserResponse

async def get_current_user(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return UserResponse(id=user_id, email=payload.get("email"))
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
