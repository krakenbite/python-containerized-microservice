ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

ARG APP_VERSION
ARG UID=10001

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update && apt install curl -y

WORKDIR /app
COPY logging.yaml .
RUN --mount=type=bind,source=dist/containerized_microservice-${APP_VERSION}-py3-none-any.whl,target=containerized_microservice-${APP_VERSION}-py3-none-any.whl \
    --mount=type=cache,target=/root/.cache/pip \
    pip install containerized_microservice-${APP_VERSION}-py3-none-any.whl

# Create and switch to non-privileged user to run the application.
# See https://docs.docker.com/develop/develop-images/instructions/#user
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser

HEALTHCHECK CMD curl -f localhost:8080/health || exit 1

ENTRYPOINT [ "uvicorn", "containerized_microservice.app:app", \
    "--host", "0.0.0.0", \
    "--port", "8080", \
    "--log-config", "logging.yaml" ]