from fastapi import APIRouter

router = APIRouter(prefix="/create-movie", tags=["Create Movie"])

@router.post("")
def create_movie():
    return {"message": "filme criado com sucesso"}
