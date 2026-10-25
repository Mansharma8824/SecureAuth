from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine
from app.routers.auth import router as auth_rounter


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title= 'SecureAuth',
    description= 'Authontication and Authorization System',
    version= '0.1.0'
)

app.include_router(auth_rounter)

@app.get('/')
def root():
    return {
        "message": "Welcome to SecureAuth",
        "status": "running",
    }
    
@app.get('/health')
def helth_check():
    return {
        "status":"healthy",
    }