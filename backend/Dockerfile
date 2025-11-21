FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

COPY entrypoint.sh /entrypoint.sh
COPY seed.py /app/seed.py
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]
