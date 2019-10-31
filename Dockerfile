FROM python:latest

COPY . /locust_tasks

WORKDIR /locust_tasks

RUN pip install -r ./requirements.txt

EXPOSE 8089 5557 5558

RUN chmod 755 ./docker-entrypoint.sh

ENTRYPOINT [ "./docker-entrypoint.sh" ]