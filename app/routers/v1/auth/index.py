from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.models.db.user import User
from app.models.interactions.user import CreateUser
from app.utils.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/signup")
async def signup(user: CreateUser, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_user = db.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    # user.password = hash_password(user.password)

    user = User(**user.dict())

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created successfully!", "user_id": user.id}


@router.post("/login")
async def login(email: str, password: str, db: Session = Depends(get_db)):
    # Find user by email
    user = db.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user.password == password:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    # Verify password
    # if not verify_password(user.password, password):
    #     raise HTTPException(status_code=401, detail="Invalid email or password")

    # Generate and return a token (or session data)
    # (This part depends on your chosen authentication approach)

    return {"message": "Logged in successfully!", "token": "your_token_here"}
