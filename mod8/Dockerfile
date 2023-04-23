FROM python:3.10.6

RUN mkdir /app

COPY requirements.txt new_year_application/ /app/

RUN python -m pip install -r /app/requirements.txt

WORKDIR /app/

ENTRYPOINT ["python", "app.py"]