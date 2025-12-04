from fastapi.testclient import TestClient 
from main import app


def test_child():
    testclient = TestClient(app)
    response1 = testclient.post("/child/add", json=dict(numberofclass=10, letterclass="B", age=16, name="Egor"))
    assert response1.status_code == 200
    assert response1.json() == "ok"
    response = testclient.post("/child/edit", json={"id" : 1, "skils" : "PE", "clas" : 8})
    assert response.status_code == 200
    assert response.json() == "ok"
    

def test_classroom():
    testclient = TestClient(app)
    response = testclient.post("/classroom/add", json=dict(number=585))
    assert response.status_code == 200
    assert response.json() == "ok"
    response1 = testclient.post("/classroom/edit", json={"id" : 1, "number" : 321})
    assert response1.status_code == 200
    assert response1.json() == "ok"


def test_teacher():
    testclint = TestClient(app)
    response = testclint.post("/teacher/add", json=dict(contract="sberb"))
    assert response.status_code == 200
    assert response.json() == "ok"
    response1 = testclint.post("/teacher/edit", json={"id" : 1, "contract" : "t-bank"})
    assert response1.status_code == 200
    assert response1.json() == "ok"


def test_lesson():
    testclient = TestClient(app)
    response = testclient.post("/lesson/add", json=dict(subject="rus", time="13:00:00"))
    assert response.status_code == 200
    assert response.json() == "ok"
    response1 = testclient.post("/lesson/edit", json={"id" : 1, "subject" : "Math", "time" : "12:00:00"})
    assert response1.status_code == 200
    assert response1.json() == "ok"




