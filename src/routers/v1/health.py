from fastapi import APIRouter, Request
    
router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root(request: Request) -> str:
    return "Success!"
