FROM bellsoft/liberica-openjdk-alpine-musl:17 AS base

RUN apk add --no-cache python3 py3-pip
COPY . .
RUN pip install --break-system-packages -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD gunicorn --threads=4 -b 0.0.0.0:10000 ctf.wsgi
