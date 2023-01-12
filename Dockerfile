FROM python:3.9

WORKDIR /app

COPY requirements.txt news-aggregator.py /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
