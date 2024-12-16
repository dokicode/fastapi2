FROM python:3.10-slim

COPY . .

RUN apt-get update
RUN apt-get install -y gcc python3-dev
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]