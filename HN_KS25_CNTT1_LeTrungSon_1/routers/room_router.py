from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.Room_schemas import RoomCreate, RoomResponse
from services import room_service

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("")
def get_all_rooms(db: Session = Depends(get_db)):
    rooms = room_service.get_rooms(db)
    data = [RoomResponse.model_validate(r).model_dump() for r in rooms]
    return {
        "statusCode": 200,
        "error": None,
        "message": "Lấy danh sách phòng thành công",
        "data": data,
    }


@router.post("")
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    new_room = room_service.add_room(room, db)
    data = RoomResponse.model_validate(new_room).model_dump()
    return {
        "statusCode": 201,
        "error": None,
        "message": "Thêm phòng thành công",
        "data": data,
    }
