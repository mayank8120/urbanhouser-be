from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.routers.index import main_router
from app.utils.database import get_db
from app.utils.server import server

app = server.app
session = get_db()


@app.get("/")
async def root(db: Session = Depends(get_db)):
    return {"message": "Welcome to your rental application!"}


app.include_router(main_router)
