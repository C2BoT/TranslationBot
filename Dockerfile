FROM python:3.8

WORKDIR /app

RUN apt-get update \
    && apt-get install -y git \
    && git clone https://github.com/C2BoT/tiktokinfos.git

WORKDIR /app/tiktokinfos

RUN pip install -r requirements.txt

CMD ["python", "tiktokinfo.py"]
