from models.RoomType import RoomTypeModel

def delete_room_types(room_type_id: int, db:db):
    exists = db.query(RoomTypeModel).filter(room_type_id == RoomTypeModel.id).first()
    
    if exists is None:
        return {
            
        }