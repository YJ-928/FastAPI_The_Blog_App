# Passlib imports
from passlib.context import CryptContext

# Uses CryptContext of passlib module to encrypt and decrypt passwords

# CryptContext is required to encrypt password or hide password
password_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

class Hash():

    def encrypt(password: str): # Give user given password as input
        return password_context.hash(password) # Returns hashed or encrypted password
    
    # To verify the passwords
    def verify(hashed_password, plain_password):
        return password_context.verify(plain_password,hashed_password)
    
