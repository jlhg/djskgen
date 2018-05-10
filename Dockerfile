FROM python:3.6.5
LABEL maintainer="Jourdan Rodrigues <thiagojourdan@gmail.com>"

WORKDIR /app/

COPY requirements.txt .

RUN pip install --no-cache-dir -q -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0 core.wsgi --log-file -
