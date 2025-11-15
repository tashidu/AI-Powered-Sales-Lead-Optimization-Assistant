from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    product_interest = Column(String, nullable=True)
    lead_score = Column(Integer, nullable=True)
    status = Column(String, default="new")
    created_at = Column(TIMESTAMP, server_default=func.now())
