from fastapi import APIRouter

app = APIRouter(prefix="/rooms")

@router.get("/")
def show_all_rooms(db = Depends(get_db)):
    show_all = 