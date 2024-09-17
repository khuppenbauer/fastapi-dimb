ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-alpine

RUN mkdir -p /app
WORKDIR /app

# Install system dependencies for Shapely
RUN apk update && apk add --no-cache \
    gcc \
    g++ \
    geos-dev \
    musl-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "gunicorn", "app.main:app", "--workers", "2", "--worker-class", \
      "uvicorn.workers.UvicornWorker",  "-b", "0.0.0.0:5000" ]
