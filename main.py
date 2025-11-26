from school import db, Child, Teacher, Lesson, Classroom
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
import datetime

app = FastAPI()


class Requests_body_teacher(BaseModel):
    id : int
    contract : str

class Requests_body_child(BaseModel):
    id : int
    clas : int
    skils : str

class Requests_body_lesson(BaseModel):
    id : int
    subject : str
    time : datetime.time

class Requests_body_classroom(BaseModel):
    id : int
    number : int


@app.post("/edit/lesson")
def edit_lesson(edit_lesson_filld : Requests_body_lesson):
    lesson = db.query(Lesson).filter(Lesson.id == edit_lesson_filld.id).first()
    lesson.subject = edit_lesson_filld.subject
    lesson.time = edit_lesson_filld.time
    db.commit()
    return "ok"



@app.post("/edit/teacher")
def edit_teacher(edit_teacher_filld : Requests_body_teacher):
    teacher = db.query(Teacher).filter(Teacher.id == edit_teacher_filld.id).first()
    teacher.contract = edit_teacher_filld.contract
    db.commit()
    return "ok"

@app.post("/edit/classroom")
def edit_classom(edit_classroom_filled : Requests_body_classroom):
    classroom = db.query(Classroom).filter(Classroom.id == edit_classroom_filled.id).first()
    classroom.number = edit_classroom_filled.number
    db.commit()
    return "ok"


@app.post("/edit/child")
def edit_child(edit_child_filld : Requests_body_child):
    child = db.query(Child).filter(Child.id == edit_child_filld.id).first()
    child.clas = edit_child_filld.clas
    child.skils = edit_child_filld.skils
    db.commit()
    return "ok"


@app.get("/app/child/{id}")
def get_child(id : int):
    child = db.query(Child).filter(Child.id == id).first()
    print(child)
#   return {"name" : child.name, "id" : child.id, "age" : child.age}
    return child

@app.get("/app/teacher/{id}")
def get_teacher(id : int):
    teacher = db.query(Teacher).filter(Teacher.id == id).first()
    print(teacher)
    return {"name" : teacher.name, "age" : teacher.age, "skils" : teacher.skils, "contract" : teacher.contract}

@app.get("/app/lesson/{id}")
def get_lesson(id : int):
    lesson = db.query(Lesson).filter(Lesson.id == id).first()
    print(lesson)
    return {"subject" : lesson.subject, "time" : lesson.time}

@app.get("/app/classroom/{id}")
def get_classroom(id : int):
    classroom = db.query(Classroom).filter(Classroom.id == id).first()
    print(classroom)
    return {"number" : classroom.number}

