FROM python:3
LABEL authors="iyuershov"

ADD requirements.txt /app/requirements.txt
ADD manage.py /app/manage.py
ADD album /app/album
ADD album_api /app/album_api
WORKDIR /app
RUN mkdir data
RUN mkdir static
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV DJANGO_SUPERUSER_PASSWORD "Place-Supersecret-Passw0rd-Here"
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata initial_data.json
RUN python manage.py createsuperuser \
    --no-input \
    --username admin \
    --email blank@email.com
RUN python manage.py collectstatic
RUN python manage.py test

CMD ["gunicorn", "album.asgi:application", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8888"]
