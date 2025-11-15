from fastapi import FastAPI

# Import DB session and models
from .db.session import Base, engine
from .models import lead

# Create DB tables
# This will create the tables defined in your models if they don't exist.
# For production, you would use a migration tool like Alembic.
lead.Base.metadata.create_all(bind=engine)

# Import routers from API modules
from .api.leads import router as leads_router
from .api.appointments import router as appointments_router
from .api.ads import router as ads_router
from .api.transcripts import router as transcripts_router
from .api.scripts import router as scripts_router

app = FastAPI(
    title="AI Sales Assistant",
    version="1.0.0"
)

# Register routers
app.include_router(leads_router, prefix="/leads", tags=["Leads"])
app.include_router(appointments_router, prefix="/appointments", tags=["Appointments"])
app.include_router(ads_router, prefix="/ads", tags=["Ads"])
app.include_router(transcripts_router, prefix="/transcripts", tags=["Transcripts"])
app.include_router(scripts_router, prefix="/scripts", tags=["Scripts"])

@app.get("/")
def root():
    return {"status": "AI Sales Backend Running!"}