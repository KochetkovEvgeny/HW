from fastapi import APIRouter
from school import db, Teacher 
from pydantic import BaseModel 

router_teacher = APIRouter(prefix="/teacher", tags=["teacher"])

class Requests_body_teacher(BaseModel):
    id : int
    contract : str

class Requests_add_teacher(BaseModel):
    contract : str 

@router_teacher.post("/add")
def add_teacher(add_teacher_info : Requests_add_teacher):
    teacher = Teacher(contract=add_teacher_info.contract)
    db.add(teacher)
    db.commit()
    return "ok"

@router_teacher.post("/edit")
def edit_teacher(edit_teacher_filld : Requests_body_teacher):
    teacher = db.query(Teacher).filter(Teacher.id == edit_teacher_filld.id).first()
    teacher.contract = edit_teacher_filld.contract
    db.commit()
    return "ok"

@router_teacher.get("/{id}")
def get_teacher(id : int):
    teacher = db.query(Teacher).filter(Teacher.id == id).first()
    print(teacher)
    return teacher 


