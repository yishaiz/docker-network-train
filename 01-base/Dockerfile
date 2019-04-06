FROM python:3.4-alpine

MAINTAINER Yishai z.

ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

EXPOSE 5000










# RUN useradd -ms /bin/bash user
# USER user



# COPY ./requirements.txt .

# RUN apk add --no-cache python3 && \
#     python3 -m ensurepip && \
#     rm -r /usr/lib/python*/ensurepip && \
#     pip3 install --upgrade pip setuptools && \
#     if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#     if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#     rm -r /root/.cache

# RUN pip install -r requirements.txt




# FROM alpine:3.9

# MAINTAINER Yishai z.

# COPY ./requirements .

# RUN apk add --no-cache python3 && \
#     python3 -m ensurepip && \
#     rm -r /usr/lib/python*/ensurepip && \
#     pip3 install --upgrade pip setuptools && \
#     if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
#     if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
#     rm -r /root/.cache

# RUN pip3 install -r requirements

# COPY ./app .

# CMD ["python3", "app.py"]
# EXPOSE 5000