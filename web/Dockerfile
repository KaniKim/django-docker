FROM nginx:1.19.8-alpine

ADD ./web/nginx.conf /etc/nginx/nginx.conf
ADD ./web/default.conf /etc/nginx/sites-available/default
ADD ./web/default.conf /etc/nginx/sites-enabled/default

RUN mkdir /var/www
RUN mkdir /var/www/front
RUN mkdir /var/www/static