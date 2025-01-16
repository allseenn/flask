# Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
import uvicorn, os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: bool


tasks = []
tasks.append(Task(id=1, title="Title 1", description="Description 1", status=True))

@app.get('/')
async def index():
    return "Hello"

@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/tasks/{title}/{description}/')
async def post_task(title: str, description: str):
    task = Task(id=len(tasks) + 1, title=title, description=description, status=False)
    tasks.append(task)
    return task

@app.put('/tasks/{id}/{title}/{description}/{status}')
async def put_task(id: int, title: str, description: str, status: bool):
    for task in tasks:
        if task.id == id:
            task.title = title
            task.description = description
            task.status = status
            return task
    raise HTTPException(status_code=404, detail='Not correct format') 

@app.delete('/tasks/{id}/')
async def delete_task(id: int):
   for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return {"message": f"Task {id} deleted"}
        else:
            raise HTTPException(status_code=404, detail='Not deleted') 


if __name__ == "__main__":
    filename = os.path.splitext(os.path.basename(__file__))[0]
    app_name = f"{filename}:app"
    uvicorn.run(app_name, host="0.0.0.0", port=8000, reload=True)

