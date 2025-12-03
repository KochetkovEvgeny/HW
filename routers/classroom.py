from fastapi import APIRouter 
from pydantic import BaseModel
from school import db, Classroom 

router_classroom = APIRouter(prefix="/classroom", tags=["classroom"])


class Requests_add_classroom(BaseModel):
    number : int  

class Requests_body_classroom(BaseModel):
    id : int
    number : int

@router_classroom.post("/add")
def add_classroom(add_classroom_info = Requests_add_classroom):
    classroom = Classroom(number=add_classroom_info.number)
    db.add(classroom)
    db.commit()
    return "ok"

@router_classroom.post("/edit")
def edit_classom(edit_classroom_filled : Requests_body_classroom):
    classroom = db.query(Classroom).filter(Classroom.id == edit_classroom_filled.id).first()
    classroom.number = edit_classroom_filled.number
    db.commit()
    return "ok"

@router_classroom.get("/{id}")
def get_classroom(id : int):
    classroom = db.query(Classroom).filter(Classroom.id == id).first()
    print(classroom)
    return classroom
