FROM nginx:stable-alpine
RUN apk update && \
    apk add --no-cache git bash && \
    rm -rf /var/cache/apk/*

COPY src/ /usr/share/nginx/html
COPY ./setup.sh /tmp/setup.sh

RUN chmod u+x /tmp/setup.sh
RUN sh /tmp/setup.sh
EXPOSE 80
