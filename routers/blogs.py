''' Router file for our blog route '''
# Fastapi imports
from fastapi import APIRouter, status, Depends
# SqlAlchemy imports
from sqlalchemy.orm import session
# Typing imports
from typing import List
# Local imports
from blog.models import get_session
from blog.schemas import BlogSchema, DisplayBlog, UserSchema
from repository.blogqueries import create_new_blog, update_blog_id, get_all_blogs, get_blog_id, destroy_all_blogs, destroy_blog_id
from blog.oauth2 import get_current_user


# Create a router instance
router = APIRouter(
    prefix = "/blog", # We can add prefix, so '/blog' now becomes just '/' below
    tags = ["Blogs"] # Common tag for all routes
)

''' current_user: UserSchema = Depends(get_current_user) 
To Lock all blog routes behind authentication. i.e.
Unless user authenticates himself he cannot perform blog operations '''

# Create blog
@router.post('/create',status_code = status.HTTP_201_CREATED)
async def create_blog(new_blog: BlogSchema, db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return create_new_blog(new_blog,db)

# Update blog
@router.put('/update/{id}', status_code = status.HTTP_302_FOUND)
async def update_blog(id: int, blog: BlogSchema, db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return update_blog_id(id,blog,db)

# Retrieve blog list
# Here we require list response model, List is imported from typing
@router.get('/', status_code = status.HTTP_200_OK, response_model = List[DisplayBlog])
async def fetch_blogs(db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return get_all_blogs(db)

# Retrieve blog using id
@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = DisplayBlog)
async def fetch_blog_id(id: int, db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return get_blog_id(id,db)
    
# Delete blogs
@router.delete('/delete', status_code = status.HTTP_200_OK)
async def delete_blogs(db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return destroy_all_blogs(db)

# Delete blog using id
@router.delete('delete/{id}', status_code = status.HTTP_200_OK)
async def delete_blog_id(id: int, db: session = Depends(get_session), current_user: UserSchema = Depends(get_current_user)):
    return destroy_blog_id(id,db)
