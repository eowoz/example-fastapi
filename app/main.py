
# Python API developement - Comprehensive Course for Beginners
# Reference : https://www.youtube.com/watch?v=0sOvCWFmrtA


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from .database import engine
from .routers import post, user, auth, vote
from . import models
from .config import settings




# Commenting below line after adding alembic it will take care of creating and upgrading tables
# models.Base.metadata.create_all(bind=engine) #this will create table if does not exist

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
    
@app.get("/")
async def root():
    return {"message": "welcome to my fastapi implemention. Deploying using CICD pipeline!! Check /doc or /redoc for documentation."}





 