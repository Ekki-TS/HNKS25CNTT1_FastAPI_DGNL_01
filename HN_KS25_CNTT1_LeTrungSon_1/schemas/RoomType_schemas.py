from pydantic import BaseModel, Field

class RoomTypeModel(BaseModel):
    id: int = Field(...)
    name: str = Field(...)