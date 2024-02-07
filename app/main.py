from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.routers.index import main_router
from app.utils.database import get_db

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",  # Adjust for your frontend origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(db: Session = Depends(get_db)):
    # Use the database session object within this function
    # ...
    return {"message": "Welcome to your rental application!"}


app.include_router(main_router)
