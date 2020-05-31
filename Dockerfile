FROM python:3.7

WORKDIR /mydir

COPY . .

RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt

CMD ["pytest", "tests/", "-v", "--ignore=tests/opencartadmin"]
