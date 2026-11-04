from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

from app.Schemas.user import UserCreate, UserResponse
from app.Schemas.auth import UserLogin, TokenResponse

from app.core.pass_security import hash_password, verify_password
from app.core.token_security import create_access_token


# craete router
router = APIRouter(
    prefix='/auth',
    tags= ["Authentication"]
)

@router.post("/register", 
             response_model=UserResponse, 
             status_code=status.HTTP_201_CREATED)

def register_user(user_data : UserCreate, db: Session = Depends(get_db)):
    # 1. check whether the email is already exists
    existing_email = db.scalar(select(User).where(User.email == user_data.email))
    
    if existing_email:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail= "Email already registered",
        )
        
    # Todo - 2. Hased password
    hashed_password = hash_password(user_data.password)
    
    # 3. Create a SQLAlchomy User object 
    new_user = User(
        username = user_data.username,
        email = user_data.email,
        hashed_password = hashed_password
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


# Create Login API 
@router.post("/login", 
            response_model=TokenResponse,
            status_code=status.HTTP_200_OK
            )

def user_login(user_data : UserLogin, db : Session = Depends(get_db)):
    # status for email
    user = db.scalar(select(User).where(User.email == user_data.email))
    
    password = verify_password(user_data.password, user.hashed_password)
    
    if user is None or  not password :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    if not user.is_active :
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail= "Account is inactive"
        )
        
    token = create_access_token(user.id)
    
    return TokenResponse(access_token=token)
    
    
    
    
        
    
        
    