FROM ubuntu:latest

WORKDIR /mydir

COPY . .

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt

CMD ["pytest", "ssh_paramiko/", "-v"]
