from fastapi import APIRouter

from app.models.db.property import Property
from app.utils.database import get_db

router = APIRouter(
    prefix="/search_list",
    tags=["Search List"],
)


@router.get("/")
async def get_search_list():
    db = get_db()

    city_state_pairs = db.query(Property.city, Property.state).distinct().all()

    pairs = []
    for city, state in city_state_pairs:
        unique_pair = {
            "city": city,
            "state": state
        }
        pairs.append(unique_pair)

    if not pairs:
        return {"message": "No data found"}, 404

    return pairs
