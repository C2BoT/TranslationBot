FROM python:3.8

WORKDIR /app

COPY tiktokinfo.py .

RUN pip install telebot

CMD ["python", "tiktokinfo.py"]
