FROM alpine:3.14
RUN apk add --no-cache python3 py3-pip

RUN mkdir -p /home/app

COPY ./server /home/app

# set default dir so that next commands executes in /home/app dir
WORKDIR /home/app

CMD ["python3", "simple-server.py"]
