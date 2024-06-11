FROM python:3.10-slim-bullseye

RUN apt-get update \
  && apt-get install -y --fix-missing --no-install-recommends --no-install-suggests \
  build-essential ffmpeg build-essential pkg-config \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --requirement /app/requirements.txt
COPY . /app

CMD ["python3", "consumer.py"]