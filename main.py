from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Learning Pydantic"
    admin_email: str = "admin@gmail.com"


def get_settings():
    return Settings()

@app.get('/')
def home():
    return{"message": "Hello World!"}

@app.post('/signup')
def signup(user: UserSignup):
    return {"message": f"User {user.username} signed up successfully"}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings