URL = "postgresql://postgres:my_password@127.0.0.1:5432/db"

from sqlalchemy import create_engine, Column, Integer, String, Time, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
import datetime

class base(DeclarativeBase):
    pass


child_lesson = Table(
    "child_lesson", 
    base.metadata,
    Column("child_id", ForeignKey("children.id"), primary_key=True),
    Column("lesson_id", ForeignKey("lessons.id"), primary_key=True)
)

class Child(base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True)
    numberofclass = Column(Integer)
    letterclass = Column(String)
    age = Column(Integer)
    name = Column(String)

    classroom_id = Column(Integer, ForeignKey("classrooms.id"))
    classroom = relationship("Classroom", back_populates="children")

    lessons = relationship("Lesson", secondary=child_lesson, back_populates="children")

class Teacher(base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    skils = Column(String)
    contract = Column(String)
    name = Column(String)
    age = Column(Integer)

    lessons = relationship("Lesson", back_populates="teacher")
    classrooms = relationship("Classroom", back_populates="teacher")


class Lesson(base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    time = Column(Time)

    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    classroom_id = Column(Integer, ForeignKey("classrooms.id"))

    teacher = relationship("Teacher", back_populates="lessons")
    classroom = relationship("Classroom", back_populates="lessons")
    children = relationship("Child", secondary=child_lesson, back_populates="lessons")

class Classroom(base):
    __tablename__ = "classrooms"
    id = Column(Integer, primary_key=True)
    number = Column(Integer)

    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher", back_populates="classrooms")
    lessons = relationship("Lesson", back_populates="classroom")
    children = relationship("Child", back_populates="classroom")


dviz = create_engine(URL)
session = sessionmaker(bind=dviz)
db = session()


if __name__ == "__main__":
    base.metadata.drop_all(bind=dviz)
    base.metadata.create_all(bind=dviz) 


    child = Child(numberofclass=10, letterclass="B", age=16, name="Egor")
    db.add(child)
    db.commit()

    teacher = Teacher(skils="Math", contract="sber", name="victor", age=33)
    db.add(teacher)
    db.commit()

    lesson = Lesson(subject="PE", time=datetime.time(10, 35, 0))
    db.add(lesson)
    db.commit()

    classroom = Classroom(number=123)
    db.add(classroom)
    db.commit()

    print("Данные добавлены.")











