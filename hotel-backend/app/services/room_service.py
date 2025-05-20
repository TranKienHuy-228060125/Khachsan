from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room import RoomCreate


def create_room(db: Session, room: RoomCreate):
    db_room = Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def get_rooms(db: Session):
    return db.query(Room).all()


def get_room(db: Session, room_id: int):
    return db.query(Room).filter(Room.id == room_id).first()


def update_room(db: Session, room_id: int, room_data: RoomCreate):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room:
        for key, value in room_data.dict().items():
            setattr(db_room, key, value)
        db.commit()
        db.refresh(db_room)
    return db_room


def delete_room(db: Session, room_id: int):
    db_room = db.query(Room).filter(Room.id == room_id).first()
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room