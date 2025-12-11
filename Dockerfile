FROM python:3.12

WORKDIR /app
COPY pyproject.toml /app 
COPY poetry.lock /app

RUN pip install poetry setuptools
RUN poetry install 
COPY . . 




CMD ["poetry", "run","uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]


