FROM python:3.9.0-slim-buster
COPY . .
RUN pip3 install -r requirements.txt
CMD python wrong_keyboard_bot.py