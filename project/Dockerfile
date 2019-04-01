FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN apk update && apk upgrade
RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev make gcc
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade -r requirements.txt
EXPOSE 5000
CMD gunicorn --bind 0.0.0.0:5000 wsgi