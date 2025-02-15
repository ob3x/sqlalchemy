from datetime import datetime

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from model import TodosCreate, Todos
from db import get_db
from tables import TodosDB

app = FastAPI()

@app.get("/todo-list/", response_model=list[Todos])
def read_todos(db : Session = Depends(get_db)):
    all_todos = db.query(TodosDB).order_by(TodosDB.id).all()

    if not all_todos:
        raise HTTPException(status_code=404, detail="Error, todo not found")
    
    return all_todos

@app.post("/create-todo/", response_model=Todos)
def create_todo(todo : TodosCreate, db : Session = Depends(get_db)):
    todo.hour = datetime.now().strftime("%H:%M:%S")
    new_todo = TodosDB(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@app.put("/edit-todo/", response_model=Todos)
def edit_todo(todo_id : int, todo : TodosCreate, db : Session = Depends(get_db)):
    edit_todo = db.query(TodosDB).filter(TodosDB.id == todo_id).first()

    if not edit_todo:
        raise HTTPException(status_code=404, detail="Error, todo not found")
    
    edit_todo.title = todo.title
    edit_todo.hour = datetime.now().strftime("%H:%M:%S")
    edit_todo.description = todo.description
    edit_todo.edited = True
    db.commit()
    db.refresh(edit_todo)
    return edit_todo
    

@app.delete("/delete-todo/")
def delete_todo(todo_id : int, db : Session = Depends(get_db)):
    remove_todo = db.query(TodosDB).filter(TodosDB.id == todo_id).first()

    if not remove_todo:
        raise HTTPException(status_code=404, detail="Error, todo not found")
    
    db.delete(remove_todo)
    db.commit()
    
    return remove_todo

if __name__ == "__main__":
    uvicorn.run(app)