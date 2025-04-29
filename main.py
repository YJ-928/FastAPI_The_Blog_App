'''Main file to run the Blog Application'''
# FastAPI imports
from fastapi import FastAPI
# Local imports
from routers import blogs,users,authentication

# Fastapi app instance
app = FastAPI()

# Include our created routers paths in the app instance
app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)

# Base path
@app.get('/', tags = ["root"])
async def index():
    return {'Welcome':'To Blog App'}
