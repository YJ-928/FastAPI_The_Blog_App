# SqlAlchemy imports
from sqlalchemy import create_engine,Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
# Local imports
from blog.database import DATABASE_URL


# Base instance
Base = declarative_base()

# User model using base instance
class UserModel(Base):
    # Tablename
    __tablename__ = "users"
    # Columns
    user_id = Column(Integer, primary_key = True, index = True) # Indexing is done automatically
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    password = Column(String, nullable = False)

    # To establish relationship with BlogModel, and sync changes
    blogs = relationship("BlogModel", back_populates = "creator")

# Blog model using base instance
class BlogModel(Base):
    # Tablename
    __tablename__ = "blogs"
    # Columns
    blog_id = Column(Integer, primary_key = True, index = True) # ie DB generates id seq without manual input
    title = Column(String, nullable = False)
    body = Column(String, nullable = False)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey(UserModel.user_id)) # Foreign key column

    # To establish a relationship with UserModel. As user who is creator of this blog
    creator = relationship("UserModel", back_populates = "blogs")

# Create an engine, using database url
Engine = create_engine(DATABASE_URL)

# Create sessionmaker instance, bind engine to it
SessionCreator = sessionmaker(bind = Engine, autoflush = False, autocommit = False)

# Create tables in database using defined models
Base.metadata.create_all(Engine)

# Create a session manager as a generator
# Using this we can create database instance
def get_session():
    session = SessionCreator()
    try:
        yield session
    finally:
        session.close()

