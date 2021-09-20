# start from base
FROM ubuntu:18.04
LABEL maintainer="umashankar thakur usthakur41@gmail.com"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENV FLASK_APP=/app/app.py
ENV PORT=5000
ENV HOST=0.0.0.0
ENTRYPOINT python -m flask run -h $HOST -p $PORT
