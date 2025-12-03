from fastapi import APIRouter
from school import db, Child
from pydantic import BaseModel

router_child = APIRouter(prefix="/child", tags=["child"])

class Requests_body_child(BaseModel):
    id : int
    clas : int
    skils : str

class Requests_add_child(BaseModel):
    numberofclass : int
    letterclass : str
    age : int
    name : str
    

@router_child.post("/add")
def add_child(add_child_info : Requests_add_child):
    child = Child(numberofclass=add_child_info.numberofclass, letterclass=add_child_info.letterclass, age=add_child_info.age, name=add_child_info.name)
    db.add(child)
    db.commit()
    return "ok"



@router_child.post("/edit")
def edit_child(edit_child_filld : Requests_body_child):
    child = db.query(Child).filter(Child.id == edit_child_filld.id).first()
    child.clas = edit_child_filld.clas
    child.skils = edit_child_filld.skils
    db.commit()
    return "ok"

@router_child.get("/{id}")
def get_child(id : int):
    child = db.query(Child).filter(Child.id == id).first()
    print(child)
#   return {"name" : child.name, "id" : child.id, "age" : child.age}
    return child