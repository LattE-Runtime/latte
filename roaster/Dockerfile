FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -e . \
    --extra-index-url https://download.pytorch.org/whl/cpu

ENTRYPOINT ["python", "-m", "latte_roaster"]