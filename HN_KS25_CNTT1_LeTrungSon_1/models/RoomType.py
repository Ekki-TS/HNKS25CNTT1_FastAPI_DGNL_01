from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class RoomTypeModel(Base):
    __tablename__ = "room_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    rooms = relationship("RoomModel", back_populates="room_type")
