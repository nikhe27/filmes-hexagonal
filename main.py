from fastapi import FastAPI
from adapters.api.routers import create_movie, search_movie

app = FastAPI(
    title="Filmes Hexagonal API",
    description="API para criação e busca de filmes",
    version="1.0.0"
)

app.include_router(create_movie.router)
app.include_router(search_movie.router)
