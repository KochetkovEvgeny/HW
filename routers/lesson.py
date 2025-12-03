from fastapi import APIRouter
from school import db, Lesson
from pydantic import BaseModel
import datetime

router_lesson = APIRouter(prefix="/lesson", tags =["lesson"])

class Requests_body_lesson(BaseModel):
    id : int
    subject : str
    time : datetime.time

class Requests_add_lesson(BaseModel):
    subject : str
    time : datetime.time

@router_lesson.post("/add")
def add_lesson(add_lesson_info : Requests_add_lesson):
    lesson = Lesson(subject=add_lesson_info.subject, time=add_lesson_info.time)
    db.add(lesson)
    db.commit()
    return "ok"


@router_lesson.post("/edit")
def edit_lesson(edit_lesson_filld : Requests_body_lesson):
    lesson = db.query(Lesson).filter(Lesson.id == edit_lesson_filld.id).first()
    lesson.subject = edit_lesson_filld.subject
    lesson.time = edit_lesson_filld.time
    db.commit()
    return "ok"

@router_lesson.get("/{id}")
def get_lesson(id : int):
    lesson = db.query(Lesson).filter(Lesson.id == id).first()
    print(lesson)
    return lesson 
