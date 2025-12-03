from fastapi import FastAPI, Query, Path
from routers.teacher import router_teacher
from routers.child import router_child
from routers.classroom import router_classroom
from routers.lesson import router_lesson


app = FastAPI()

app.include_router(router_teacher)
app.include_router(router_child)
app.include_router(router_classroom)
app.include_router(router_lesson)



