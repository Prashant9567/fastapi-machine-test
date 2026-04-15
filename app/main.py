from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

# Include routes
app.include_router(router, prefix="/api")