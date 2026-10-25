from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserCreate(BaseModel):
    username : str = Field(min_length=3, max_length=50)
    email : EmailStr
    password : str = Field(min_length=6, max_length=128)
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    username: str
    email: EmailStr
    is_active: bool
    role: str
    
