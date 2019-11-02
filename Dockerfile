FROM python:3.6.9
LABEL maintainer="Jourdan Rodrigues <thiagojourdan@gmail.com>"

WORKDIR /app/

COPY requirements.txt .

RUN pip install --no-cache-dir -q -r requirements.txt

COPY . .
