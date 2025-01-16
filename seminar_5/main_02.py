import uvicorn, os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import HTMLResponse


app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str

class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre


movies = []
movies.append(Movie(id=1, title="Titanic", description="Description 1", genre=Genre(id=1, name="Drama")))
movies.append(Movie(id=2, title="Police academy", description="Description 2", genre=Genre(id=2, name="Comedy")))
movies.append(Movie(id=3, title="Titanic", description="Description 1", genre=Genre(id=3, name="Fantasy")))

@app.get('/', response_class=HTMLResponse)
async def index():
    return """
<h1>Задача № 2</h1>
<ol>
    <li>Создать API для получения списка фильмов по жанру. Приложение должно иметь возможность получать список фильмов по заданному жанру</li>
    <li>Создайте модуль приложения и настройте сервер и маршрутизацию</li>
    <li>Создайте класс Movie с полями id, title, description и genre</li>
    <li>Создайте список movies для хранения фильмов</li>
    <li>Создайте маршрут для получения списка фильмов по жанру (метод GET)</li>
    <li>Реализуйте валидацию данных запроса и ответа</li>
</ol>
"""

@app.get("/movies/", response_model=List[Movie])
async def get_movie(genre_id: int = None):
    for movie in movies:
        if movie.genre.id == genre_id:
            return movie
        else:
            return movies
    raise HTTPException(status_code=404, detail='Movie not found')


if __name__ == "__main__":
    filename = os.path.splitext(os.path.basename(__file__))[0]
    app_name = f"{filename}:app"
    uvicorn.run(app_name, host="0.0.0.0", port=8000, reload=True)

