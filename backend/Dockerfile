FROM ubuntu:22.04

RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y python3

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

# init db
WORKDIR /app/database
RUN python3 init_db.py
WORKDIR /app

EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "controller.py" ]
