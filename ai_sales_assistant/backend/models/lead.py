from sqlalchemy import Column, Integer, String, Float
from ..db.session import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company = Column(String, index=True, nullable=True)
    job_title = Column(String, index=True, nullable=True)
    lead_score = Column(Float, nullable=True)
    status = Column(String, default="new")