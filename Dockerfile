FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install apache2 -y
RUN apt-get install apache2-utils -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get clean
COPY /app /var/www/html/

WORKDIR /var/www/html/
RUN pip install -r requirements.txt
RUN rm index.html
RUN python3 run.py

EXPOSE 80
CMD ["apache2ctl","-D","FOREGROUND"]