from fastapi import FastAPI
from app.adapters.api.routers import create_movie, search_movie

app = FastAPI(title="Filmes Hexagonal API")

# Rota de saúde
@app.get("/")
def health_check():
    return {"status": "online"}

# Incluir os routers da API
app.include_router(create_movie.router)
app.include_router(search_movie.router)
