FROM python:3.8

WORKDIR /app

COPY tiktokinfo.py .

RUN pip install --no-cache-dir telebot \
    && pip install --no-cache-dir python-telegram-bot \
    && pip install --no-cache-dir pyTelegramBotAPI==3.8.2 \
    && pip install --no-cache-dir requests

CMD ["python", "tiktokinfo.py"]
