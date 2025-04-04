FROM python:3.12
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ADD . /app

RUN uv sync --frozen
RUN uv run main.py
