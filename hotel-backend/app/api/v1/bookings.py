from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.booking import BookingCreate, BookingOut
from app.services import booking_service
from app.middleware.auth import get_current_user
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BookingOut)
def book_room(booking: BookingCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return booking_service.create_booking(db, booking, user_id=current_user.id)

@router.get("/me", response_model=list[BookingOut])
def list_my_bookings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return booking_service.get_user_bookings(db, user_id=current_user.id)

@router.get("/{booking_id}", response_model=BookingOut)
def get_booking_detail(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    booking = booking_service.get_booking(db, booking_id)
    if not booking or booking.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Booking not found or unauthorized")
    return booking

@router.delete("/{booking_id}")
def cancel_booking(booking_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    booking = booking_service.get_booking(db, booking_id)
    if not booking or booking.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="Booking not found or unauthorized")
    return booking_service.delete_booking(db, booking_id)