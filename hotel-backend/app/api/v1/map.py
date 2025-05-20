from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/key")
def get_maps_key():
    return {"api_key": settings.GOOGLE_MAPS_API_KEY}