from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import room_type_service

router = APIRouter(prefix="/room-types", tags=["room-types"])


@router.delete("/{room_type_id}")
def delete_room_type(room_type_id: int, db: Session = Depends(get_db)):
    room_type_service.delete_room_type(room_type_id, db)
    return {
        "statusCode": 200,
        "error": None,
        "message": "Xóa loại phòng thành công",
        "data": None,
    }
