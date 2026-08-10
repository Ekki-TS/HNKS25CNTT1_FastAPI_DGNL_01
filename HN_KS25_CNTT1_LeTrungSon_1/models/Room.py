from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class RoomModel(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    room_no = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    room_type_id = Column(Integer, ForeignKey("room_types.id"), nullable=False)

    room_type = relationship("RoomTypeModel", back_populates="rooms")
