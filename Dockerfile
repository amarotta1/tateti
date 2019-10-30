FROM python:3

RUN git clone https://github.com/amarotta1/tateti.git

WORKDIR /tateti

RUN pip install parameterized

RUN pip install -r requirements.txt

CMD ["python3", "./test_tateti.py"]