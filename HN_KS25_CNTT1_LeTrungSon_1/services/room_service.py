from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.Room import RoomModel
from models.RoomType import RoomTypeModel
from schemas.Room_schemas import RoomCreate


def add_room(room: RoomCreate, db: Session):
    room_type = db.query(RoomTypeModel).filter(RoomTypeModel.id == room.room_type_id).first()
    if room_type is None:
        raise HTTPException(status_code=400, detail="Loại phòng không tồn tại")

    existed = db.query(RoomModel).filter(RoomModel.room_no == room.room_no).first()
    if existed is not None:
        raise HTTPException(status_code=400, detail="Số phòng bị trùng")

    new_room = RoomModel(
        room_no=room.room_no,
        price=room.price,
        room_type_id=room.room_type_id,
    )
    db.add(new_room)
    db.commit()
    db.refresh(new_room)
    return new_room


def get_rooms(db: Session):
    return db.query(RoomModel).all()
