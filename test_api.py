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
    


