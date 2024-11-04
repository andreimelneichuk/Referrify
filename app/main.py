from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, crud, auth, dependencies
from .config import get_db
from datetime import timedelta

app = FastAPI()

@app.post("/register/", response_model=schemas.UserResponse)
async def register_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    hashed_password = auth.get_password_hash(user.password)
    user = await crud.create_user(db, email=user.email, password=hashed_password)
    return user

@app.post("/token/")
async def login_for_access_token(form_data: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user(db, email=form_data.email)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(data={"sub": user.id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/referral/")
async def create_referral_code(data: schemas.ReferralCodeCreate, db: AsyncSession = Depends(get_db), user: schemas.UserResponse = Depends(dependencies.get_current_user)):
    existing_code = await crud.get_referral_code(db, user_id=user.id)
    if existing_code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Referral code already exists.")
    code = await crud.create_referral_code(db, user_id=user.id, expiration_date=data.expiration_date)
    return code
