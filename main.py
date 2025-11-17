from school import db, Child, Teacher, Lesson, Classroom
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/app/child/{id}")
def get_child(id : int):
    child = db.query(Child).filter(Child.id == id).first()
    print(child)
    return {"name" : child.name, "id" : child.id, "age" : child.age}

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

