from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.RoomType import RoomTypeModel
from models.Room import RoomModel


def delete_room_type(room_type_id: int, db: Session):
    room_type = db.query(RoomTypeModel).filter(RoomTypeModel.id == room_type_id).first()
    if room_type is None:
        raise HTTPException(status_code=404, detail="Loại phòng không tồn tại")

    has_rooms = db.query(RoomModel).filter(RoomModel.room_type_id == room_type_id).first()
    if has_rooms is not None:
        raise HTTPException(status_code=400, detail="Không thể xóa vì vẫn còn phòng thuộc loại phòng này")

    db.delete(room_type)
    db.commit()
    return room_type
