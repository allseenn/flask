import re
from fastapi import FastAPI, HTTPException, Request, Form
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="seminar_5/templates")

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
    User(id=3, name='Peter', email='peter@mail.ru', password='Ddpetersdfsd1'),
    User(id=4, name='John', email='john2@mail.ru', password='Ddpetersdfsd1')
]

@app.get('/', response_class=HTMLResponse, summary="Display form", tags=['User'])
async def index(request: Request):
    return templates.TemplateResponse("user.html", {"request": request})


@app.post('/', response_model=List[User], summary="Get user by id", tags=["User"])
async def get_user(request: Request, id: str = Form(...), name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    copy_users = users.copy()
    id_users = list()
    name_users = list()
    email_users = list()
    found_users = list()
    for user in copy_users:
        if str(user.id) == id and id is not "":
            id_users.append(user)
        if user.name == name and name is not "":
            name_users.append(user)
        if user.email == email and email is not "":
            email_users.append(user)
    all_users = id_users + name_users + email_users
    if id is '' and name is '' and email is '':
        all_users = users
    for user in all_users:
        hide_user = user.clone()
        hide_user.password = "********"
        found_users.append(hide_user)
    message = f'{len(found_users)} user{"s" if len(found_users) != 1 else ""} was found'
    return templates.TemplateResponse("user.html", {"request": request, "users": found_users, 'message': message})


@app.put('/', response_model=List[User], summary="Update user", tags=["Users"])
async def put_user(request: Request, id: str = Form(...), name: str = Form(...), email: str = Form(...), password: str = Form(...)):
    found_users = list()
    for user in users:
        if str(user.id) == id:
                user.id=int(id)
                user.name=name
                user.email=email
                user.password=password
                hide_user = user.clone()
                hide_user.password = "********"
                found_users.append(hide_user)
    message = f'{len(found_users)} user{"s" if len(found_users) != 1 else ""} was changed'
    return templates.TemplateResponse("user.html", {"request": request, "users": found_users, 'message': message})



@app.delete('/', response_model=List[User], summary="Update user", tags=["Users"])
async def put_user(request: Request, id: str = Form(...)):
    found_users = list()
    for user in users:
        if str(user.id) == id:
                hide_user = user.clone()
                hide_user.password = "********"
                users.remove(user)
                found_users.append(hide_user)
    message = f'{len(found_users)} user{"s" if len(found_users) != 1 else ""} was deleted'
    return templates.TemplateResponse("user.html", {"request": request, "users": found_users, 'message': message})


if __name__ == "__main__":
    import uvicorn, os
    filename = os.path.splitext(os.path.basename(__file__))[0]
    app_name = f"{filename}:app"
    uvicorn.run(app_name, host="0.0.0.0", port=8000, reload=True)