from sqlalchemy.orm import Session

from todo.models import ToDo
from todo.database.base import get_db
from todo.main import app, templates
from fastapi import Request, Depends
from todo.config import settings


@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todos})
