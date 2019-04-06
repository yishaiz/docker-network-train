FROM python:3.4-alpine

MAINTAINER Yishai z.

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

EXPOSE 5000

