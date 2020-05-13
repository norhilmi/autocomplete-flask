# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7
RUN apt-get update -y && \
   apt-get install -y python-pip python-dev
COPY ./requirements.txt /var/www/flask-app/autocomplete/requirements.txt
COPY . /var/www/flask-app/autocomplete
WORKDIR /var/www/flask-app/autocomplete
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]