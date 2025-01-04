FROM python:3.12-alpine
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /app/src
CMD [ "python", "main.py" ]