import requests 

URL = "http://0.0.0.0:8080"



response = requests.get(f"{URL}/app/child/{1}")
print(response.content)


response1 = requests.post(f"{URL}/edit/child", json={"id" : 1, "skils" : "PE", "clas" : 8})
print(response1.content)

response2 = requests.get(f"{URL}/app/child/{1}")
print(response2.content)

response3 = requests.get(f"{URL}/app/teacher/{1}")
print(response3.content)

response4 = requests.post(f"{URL}/edit/teacher", json = {"id" : 1, "contract" : "t-bank"})
print(response4.content)

response5 = requests.get(f"{URL}/app/teacher/{1}")
print(response5.content)

response6 = requests.get(f"{URL}/app/lesson/{1}")
print(response6.content)

response7 = requests.post(f"{URL}/edit/lesson", json={"id" : 1, "subject" : "Math", "time" : "12:00:00"})
print(response7.content)

response8 = requests.get(f"{URL}/app/lesson/{1}")
print(response8.content)

response9 = requests.get(f"{URL}/app/classroom/{1}")
print(response9.content)

response10 = requests.post(f"{URL}/edit/classroom", json={"id" : 1 , "number" : 321})
print(response10.content)

response11 = requests.get(f"{URL}/app/classroom/{1}")
print(response11.content)

