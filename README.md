# Aquariomaniacos

Website for [http://aquariomaniacos.com.br](http://aquariomaniacos.com.br)

## Requirements

- [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

### How to use

First you should install the docker and docker-compose applications (links on requirements session).

- `docker-compose build` to build the container;
- `docker-compose up` to run the server (you can pass `-d` to run in backgroud);
- `docker-compose stop` to stop the server;
- `docker container prune -f` if you need to delete the container;
- `docker volume prune -f` if you need to delete the database;
- `docker network prune -f` if you need to delete the network;
- `docker kill $(docker ps -q)` if you need to kill all docker instances;

* The server will run on `localhost:8000`

#### Creating a superuser

You can create a superuser to access admin painel and other things, you just need to run:

- Install [python 3.x](https://www.python.org/downloads/);
- Install python-pip using `apt-get install python-pip`;
- Install the dependencies using `pip install -r requirements.txt`;
- Export env vars using `source app.env`;
- Create the user using `python manage.py createsuperuser`;

### Code Quality

We use some tools to ensure our code quality.

- `pylint`
- `django-lint`
- `pytest`
