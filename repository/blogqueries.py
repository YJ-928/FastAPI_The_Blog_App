'''Repository to store all blog route queries in the form of functons'''
# Fastapi imports
from fastapi import status,HTTPException
# SqlAlchemy imports
from sqlalchemy.orm import Session
# Local imports
from blog.models import BlogModel

def create_new_blog(new_blog,db: Session):
    '''Query function to create a new blog'''
    # Always map schemas to modeles
    new_blog_obj = BlogModel(
        title = new_blog.title,
        body = new_blog.body,
        published = new_blog.published,
        user_id = new_blog.user_id
    )
    db.add(new_blog_obj)
    db.commit()
    db.refresh(new_blog_obj) # Refresh instead of flush when using database instance
    return new_blog_obj
    
def update_blog_id(id,blog,db: Session):
    '''Query function to update a blog using id'''
    blog_exists = db.query(BlogModel).filter(BlogModel.blog_id == id)
    blog_in_db = blog_exists.first()
    if not blog_in_db:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    # model_dump() --> converts to dict
    # exclude is used to avoid confusion between blog_id & id
    blog_exists.update(blog)
    db.commit()
    return {'detail':'Blog Updated'}

def get_all_blogs(db: Session):
    '''Query function to fetch all items from database'''
    blog_list = db.query(BlogModel).all() # Returns list of all blogs
    if len(blog_list) != 0:
        return blog_list
    else:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "No blogs found")

def get_blog_id(id: int, db: Session):
    '''Query function to fetch one blog using id'''
    blog = db.query(BlogModel).filter_by(blog_id = id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")

def destroy_all_blogs(db: Session):
    '''Query function to delete all blogs'''
    blog_list = db.query(BlogModel).all() # Returns list of all blogs
    for blog in blog_list:
        db.delete(blog)
    db.commit()
    if blog_list:
        return {"detail": f"{len(blog_list)} blogs deleted"}
    else:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "No blogs found")

def destroy_blog_id(id: int, db: Session):
    '''Query function to delete one blog using id'''
    blog = db.query(BlogModel).filter_by(blog_id = id).delete()
    db.commit()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    else:
        return {'detail':f"Blog with id {id} deleted"}
    