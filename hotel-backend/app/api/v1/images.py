from fastapi import APIRouter, File, UploadFile
import requests
from app.core.config import settings

router = APIRouter()

@router.post("/upload")
def upload_image(file: UploadFile = File(...)):
    files = {"file": (file.filename, file.file, file.content_type)}
    data = {"upload_preset": "hotel_uploads"}  # cấu hình Cloudinary preset nếu có
    response = requests.post(settings.CLOUDINARY_URL, files=files, data=data)
    return response.json()