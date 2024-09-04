FROM python:3.12.5-bookworm

WORKDIR /app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY src/ .

RUN ls -Ahl

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
