FROM docker.io/library/python:3
MAINTAINER Vincent Demeester <vincent@sbr.pm>
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
