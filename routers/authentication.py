'''To authenticate the user using email and password and generate a JWTtoken'''
# Fastapi imports
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestFormStrict
# SqlAlchemy orm imports
from sqlalchemy.orm import Session
# Local imports
from blog.schemas import Login
from blog.models import get_session, UserModel
from blog.hashing import Hash
from blog.token import create_access_token

# Router instance
router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
async def login(request: OAuth2PasswordRequestFormStrict = Depends(), db: Session = Depends(get_session)):
    user = db.query(UserModel).filter(UserModel.email == request.username).first()
    if not user: # Check for user in db
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Invalid Credentials")
    # Verify user given password with stored hashed password
    if not Hash.verify(hashed_password = user.password, plain_password = request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Invalid Password")
    # Generate a JWT access_token for this user
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}