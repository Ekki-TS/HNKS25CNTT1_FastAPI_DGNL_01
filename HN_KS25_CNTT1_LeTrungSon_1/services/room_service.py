from models.Room import RoomModel
from python_core import raw_rooms

def add_rooms(new_room: RoomModel, db: db):
    exists = db.query(RoomModel).filter(new_room.room_type_id).first()
    
    if exists is None:
        return {
            status_code = 400,
            message = "Số phòng không tồn tại",
        }
    
    exists = db.query(RoomModel).filter(new_room.room_no).all()
    
    if exists:
        return {
            status_Code = 400,
            message = "Số phòng bị trùng"
        }
    
    db.add(exists)
    db.commit()
    db.refresh(exists)
    
def show_rooms(db:db):
    exists = db.query(RoomModel).all()
    
    return exists
    
def delete_rooms(room)