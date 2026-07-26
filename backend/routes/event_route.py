from fastapi import APIRouter

router = APIRouter(
    prefix="/dependencies",
    tags=["Dependencies"]
)

@router.get("/")
def get_dependencies():
    return {
        "message": "Dependency data"
    }