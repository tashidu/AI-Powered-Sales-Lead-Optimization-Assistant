from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..db.session import get_db
from ..models.lead import Lead as LeadModel
from ..services.lead_scorer import score_lead

router = APIRouter()


# Pydantic model for request body
class LeadCreate(BaseModel):
    name: str
    email: str
    company: str | None = None
    job_title: str | None = None


# Pydantic model for response
class Lead(LeadCreate):
    id: int
    lead_score: float | None = None
    status: str

    class Config:
        orm_mode = True


@router.post("/", response_model=Lead)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    """
    Receives lead data, scores it using AI, and saves it to the database.
    """
    lead_details = lead.dict()

    # Score the lead using the AI service
    lead_score = score_lead(lead_details)

    # Create a new lead instance with the score
    db_lead = LeadModel(
        name=lead.name,
        email=lead.email,
        company=lead.company,
        job_title=lead.job_title,
        lead_score=lead_score,
        status="new",
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return db_lead