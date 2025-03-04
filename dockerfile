FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

#install the app dependencies (??)
WORKDIR /app


RUN uv sync --frozen --no-cache


# Uruchamiamy aplikację
CMD ["uv", "run", "manage.py", "runserver", "localhost:8000"]
