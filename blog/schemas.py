# Pydantic imports
from pydantic import BaseModel
# Typing imports
from typing import List

# Schemas are required for request and response body

# User schema using BaseModel
class UserSchema(BaseModel):
    name: str
    email: str
    password: str

# Blog schema using pydantic BaseModel
class BlogSchema(BaseModel):
    title: str
    body: str
    published: bool
    user_id: int # ForeignKey input

# BlogList schema using BaseModel to display list of blogs created by a certian user
class DisplayUserBlogs(BaseModel):
    title: str
    body: str
    published: bool

    class Config():
        from_attributes = True

# DisplayUser response model for user to show only name and email
class DisplayUser(BaseModel):
    name: str
    email: str

    # Relationship
    blogs: List[DisplayUserBlogs] # To display a list of all blogs created by this user

    # Need to define class Config for Response Body
    class Config():
        # Enables conversion from ORM to Pydantic
        from_attributes = True

# Creating a response model (Response Body) from BaseModel
# As we dont need to display id, as we are fetching things from id itself
class DisplayBlog(BaseModel):
    title: str
    body: str
    published: bool

    # Relationship
    creator: DisplayUser # To display creator of blog by relationship

    # Conversion from orm to pydantic
    class Config():     
        from_attributes = True


# Create a LoginSchema to take email and password inputs
class Login(BaseModel):
    username: str
    password: str

# Token Schemas needed for JWT token generation
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

