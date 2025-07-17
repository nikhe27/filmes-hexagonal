from fastapi import APIRouter

router = APIRouter(prefix="/search-movie", tags=["Search Movie"])

@router.get("")
def search_movie():
    return {"message": "busca realizada com sucesso"}
