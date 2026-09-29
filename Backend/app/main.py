from fastapi import FastAPI
from app.api.routes.users import router as users_router

app = FastAPI(
    title = "SecureAuth API ",
    description = "Authentication and Authorization System",
    version = "1.0.0"
)

app.include_router(users_router)
    
    