FROM ghcr.io/astral-sh/uv:debian-slim

ENV DEBIAN_FRONTEND=noninteractive

COPY . /app

WORKDIR /app

RUN uv sync --frozen

CMD ["uv", "run", "app/main.py"]