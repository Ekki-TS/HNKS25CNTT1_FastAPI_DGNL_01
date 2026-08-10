from pydantic import BaseModel, Field, ConfigDict


class RoomTypeResponse(BaseModel):
    id: int = Field(...)
    name: str = Field(...)

    model_config = ConfigDict(from_attributes=True)
