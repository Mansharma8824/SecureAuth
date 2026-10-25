from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.Schemas.user import UserCreate, UserResponse

# craete router
router = APIRouter(
    prefix='/auth',
    tags= ["Authentication"]
)

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED,)
def register_user(user_data : UserCreate, db: Session = Depends(get_db)):
    # 1. check whether the email is already exists
    existing_email = db.scalar(select(User).where(User.email == user_data.email))
    
    if existing_email:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail= "Email already registered",
        )
        
    # Todo - 2. Hased password
    
    # 3. Create a SQLAlchomy User object 
    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = user_data.password
    )
    
    # 4. save the user to the database
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email or username already registered",
        )
        
    # 5. Return safe user information
    return new_user



        
    
        
    