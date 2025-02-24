from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "FastAPI is running!"}

@router.get("/health")
async def health_check():
    return {"status": "ok"}