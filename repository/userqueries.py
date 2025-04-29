'''Repository file to store all user queries as functions'''
# Fastapi imports
from fastapi import status,HTTPException
# SqlAlchemy imports
from sqlalchemy.orm import Session
# Local imports
from blog.models import UserModel
from blog.hashing import Hash

def create_new_user(user,db:Session):
    '''Query function to create new user'''
    # Mapping user schema to model
    new_user = UserModel(
        name = user.name,
        email = user.email,
        # Hashing password or encrypting it using Hash
        password = Hash.encrypt(user.password) # Displays encrypted or hashed out password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_id(id,user,db:Session):
    '''Query function to update user details'''
    user_exists = db.query(UserModel).filter(UserModel.user_id == id)
    user_in_db = user_exists.first()
    if not user_in_db:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
    else:
        user_exists.update(user)
        db.commit()
        return {'detail':'User Updated'}
    
def get_all_users(db:Session):
    '''Query function to fetch all users'''
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No users found")
    return users

def get_user_id(id,db:Session):
    '''Query function to fetch user using id'''
    user = db.query(UserModel).filter(UserModel.user_id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
    return user

def destroy_all_users(db:Session):
    '''Query function to delete all users'''
    user_list = db.query(UserModel).all()
    for user in user_list:
        db.delete(user)
    db.commit()
    if user_list:
        return {"detail": f"{len(user_list)} users deleted"}
    else:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "No users found")

def destroy_user_id(id,db:Session):
    '''Query function to delete user using id'''
    user = db.query(UserModel).filter_by(blog_id = id).delete()
    db.commit()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
    else:
        return {'detail':f"User with id {id} deleted"}
