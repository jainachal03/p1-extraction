FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
ENV UV_PYTHON_DOWNLOADS=never
WORKDIR /app
COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --frozen --no-dev --no-install-project
COPY schema.py extract.py cache.py service.py ./
ENV OLLAMA_BASE_URL=http://host.docker.internal:11434/v1
ENV CACHE_DB=/data/llm_cache.db
EXPOSE 8000
CMD ["/app/.venv/bin/fastapi", "run", "service.py", "--host", "0.0.0.0", "--port", "8000"]
