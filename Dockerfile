FROM python3
LABEL authors="iyuershov"

ADD requirements.txt /app/requirements.txt
ADD album /app
ADD album_api /app
WORKDIR /app
RUN mkdir data
RUN mkdir static
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "album.asgi:application", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8888"]