import re
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from fastapi.responses import HTMLResponse


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: EmailStr = Field(..., description="Email address of the user")
    password: str = Field(..., min_length=8, description="Password of the user")
    def clone(self):
        return User(id=self.id, name=self.name, email=self.email, password=self.password)

    @field_validator('password')
    def password_must_contain_uppercase(cls, v):
        if not re.search('[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search('[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search('[0-9]', v):
            raise ValueError('Password must contain at least one digit')
        return v

users = [
    User(id=1, name='John', email='john@mail.ru', password='Ddjohytnsdfs1'),
    User(id=2, name='David', email='david@mail.ru', password='Dddavidsdfsd1'),
    User(id=3, name='Peter', email='peter@mail.ru', password='Ddpetersdfsd1')
]

@app.router.get("/", response_class=HTMLResponse)
async def root():
    return """
        <h1>Задание №5</h1>
        <ol>
            <li>Создать API для удаления информации о пользователе из базы данных. Приложение должно иметь возможность принимать DELETE запросы и удалять информацию о пользователе из базы данных</li>
            <li>Создайте модуль приложения и настройте сервер и маршрутизацию</li>
            <li>Создайте класс User с полями id, name, email и password</li>
            <li>Создайте список users для хранения пользователей</li>
            <li>Создайте маршрут для удаления информации о пользователе (метод DELETE)</li>
            <li>Реализуйте проверку наличия пользователя в списке и удаление его из списка</li>
        </ol>
        """

@app.get('/user/{id}', response_model=User)
async def get_user(id: int):
    for user in users:
        if user.id == id:
            hide_user = user.clone()
            hide_user.password = "********"
            return hide_user
    raise HTTPException(status_code=422, detail="User not found")

@app.get('/users', response_model=List[User])
async def get_users():
    hide_users = []
    for user in users:
        hide_user = user.clone()
        hide_user.password = "********"
        hide_users.append(hide_user)
    return hide_users

@app.post('/users', response_model=User)
async def post_user(u: User):
    user = User(id=len(users)+1, name=u.name, email=u.email, password=u.password)
    users.append(user)
    user.password = '******'
    return user

@app.put('/users', response_model=User)
async def put_user(u: User):
    for user in users:
        if user.id == u.id:
                user.id=u.id
                user.name=u.name
                user.email=u.email
                user.password=u.password
                hide_user = user.clone()
                hide_user.password = "********"
                return hide_user
    raise HTTPException(status_code=422, detail="User not found")
        

@app.delete('/users', response_model=User)
async def delete_user(id: int):
    for user in users:
        if user.id == id:
            hide_user = user.clone()
            hide_user.password = "********"
            users.remove(user)
            return hide_user


if __name__ == "__main__":
    import uvicorn, os
    filename = os.path.splitext(os.path.basename(__file__))[0]
    app_name = f"{filename}:app"
    uvicorn.run(app_name, host="0.0.0.0", port=8000, reload=True)