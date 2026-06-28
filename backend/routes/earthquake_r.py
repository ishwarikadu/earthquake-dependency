from fastapi import APIRouter

router = APIRouter(
    prefix="/earthquakes",
    tags=["Earthquakes"]
)

@router.get("/")
def get_earthquakes():
    return {
        "message": "All earthquake events"
    }