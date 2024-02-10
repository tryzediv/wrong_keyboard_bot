FROM python:3.9.0-slim-buster as builder
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

FROM python:3.9.0-slim-buster
WORKDIR /app
COPY --from=builder /app /app
CMD python 8_ball_bot.py
