from fastapi import APIRouter, HTTPException

from app.schemas.user import UserCreate

router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)

@router.get("")
def get_user():
    return {
        "Message" : "Getting User"
    }
    
    
@router.post("")
def create_user(user : UserCreate):
    return {
        "Message": "Creating User",
        "name":user.name,
        "email" : user.email
    }

@router.get("/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "user not found"
        )
    return {
        "user" : user_id
    }
    
@router.put("/{user_id}")
def update_user(user_id:int):
    return {
        "Message" : "Updating the user"
    }
    
@router.delete("/{user_id}")
def delete_user(user_id:int):
    return{
        "Message" : "Deleting the user"
    }