FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r reqrequirements.txt

COPY . .

#CMD ["python", "manage.py", "runserver"]