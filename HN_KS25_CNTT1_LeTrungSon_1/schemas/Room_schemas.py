from pydantic import BaseModel, Field, ConfigDict
from schemas.RoomType_schemas import RoomTypeResponse


class RoomCreate(BaseModel):
    room_no: str = Field(..., min_length=4, max_length=10)
    price: float = Field(..., gt=0)
    room_type_id: int = Field(...)


class RoomResponse(BaseModel):
    id: int = Field(...)
    room_no: str = Field(..., max_length=10)
    price: float = Field(...)
    room_type: RoomTypeResponse

    model_config = ConfigDict(from_attributes=True)
