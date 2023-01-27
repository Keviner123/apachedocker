# syntax=docker/dockerfile:1
FROM ubuntu:latest

RUN apt update
RUN apt install -y apache2 
RUN apt install -y systemctl

COPY /app /var/www/html

EXPOSE 80
CMD apachectl -D FOREGROUND


