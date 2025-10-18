FROM nginx:stable-alpine
ARG flag='flag{G1T_H1d3s_Th3_S3cr3t}'

RUN apk update && \
    apk add --no-cache git bash && \
    rm -rf /var/cache/apk/*

COPY src/ /usr/share/nginx/html
COPY ./setup.sh /tmp/setup.sh

RUN sed -i 's/FLAG{flag_placeholder}/'$flag'/' /tmp/setup.sh
RUN chmod u+x /tmp/setup.sh
RUN sh /tmp/setup.sh

EXPOSE 80
