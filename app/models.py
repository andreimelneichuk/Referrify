from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class ReferralCode(Base):
    __tablename__ = "referral_codes"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    expiration_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user = relationship("User", back_populates="referral_code")

User.referral_code = relationship("ReferralCode", back_populates="user", uselist=False)
