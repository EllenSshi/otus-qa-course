FROM python:3.7

WORKDIR /mydir

COPY . .

RUN apt-get update && \
    apt-get install python3-pip -y && \
    pip3 install -r requirements.txt

CMD ["pytest", "-v", "--alluredir=allure_report"]
