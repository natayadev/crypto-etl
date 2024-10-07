FROM python:3.12-slim

WORKDIR /app

COPY ./ /app/

RUN python -m venv env
RUN pip install -r requirements.txt

CMD [ ".env/bin/python", "main.py" ]