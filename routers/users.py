''' Router file for our user route '''
# Fastapi imports
from fastapi import APIRouter,status,Depends
# SqlAlchemy imports
from sqlalchemy.orm import session
# Typing imports
from typing import List
# Local imports
from blog.models import get_session
from blog.schemas import UserSchema,DisplayUser
from repository.userqueries import create_new_user,update_user_id,get_all_users,get_user_id,destroy_all_users,destroy_user_id

# Create a router instance
router = APIRouter(
    prefix = "/user", # We can add prefix, so '/user' now becomes just '/' below
    tags = ["Users"] # And also a commom tag for all routes
)

# Create user
@router.post('/create', status_code = status.HTTP_201_CREATED, response_model = DisplayUser)
async def create_user(user:UserSchema,db:session = Depends(get_session)):
    return create_new_user(user,db)

# Update user
@router.put('/update/{id}', status_code = status.HTTP_200_OK)
async def update_user(id:int,user:UserSchema,db:session = Depends(get_session)):
    return update_user_id(id,user,db)

# Retrieve user
# Retrieving list of user, hence a list response model
@router.get('/', status_code = status.HTTP_200_OK, response_model = List[DisplayUser])
async def show_users(db:session = Depends(get_session)): # Database instance
    return get_all_users(db)

# Retrieve user using id
@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = DisplayUser)
async def show_user_id(id:int,db:session = Depends(get_session)):
    return get_user_id(id,db)

# Delete user
@router.delete('/delete', status_code = status.HTTP_200_OK)
async def delete_user(db:session = Depends(get_session)):
    return destroy_all_users(db)

# Delete user using id
@router.delete('/delete/{id}', status_code = status.HTTP_200_OK)
async def delete_user_id(id:int,db:session = Depends(get_session)):
    return destroy_user_id(id,db)
