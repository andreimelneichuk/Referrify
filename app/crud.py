from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import User, ReferralCode
import datetime

async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, hashed_password=password)
    db.add(user)
    await db.commit()
    return user

async def get_user(db: AsyncSession, email: str):
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()

async def create_referral_code(db: AsyncSession, user_id: int, expiration_date: datetime.datetime):
    code = ReferralCode(user_id=user_id, expiration_date=expiration_date)
    db.add(code)
    await db.commit()
    return code
