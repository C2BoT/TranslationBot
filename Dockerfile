FROM python:3.8

WORKDIR /app

COPY tiktokinfo.py .

RUN pip install telebot
RUN pip install python-telegram-bot
RUN pip install pyTelegramBotAPI==3.8.2
RUN pip install bs4
RUN pip install BeautifulSoup
RUN pip install datetime
RUN pip install requests

CMD ["python", "tiktokinfo.py"]
