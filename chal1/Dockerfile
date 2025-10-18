FROM nginx:stable-alpine
ARG flag="flag{my_first_spidering_flag}"

COPY src/ /usr/share/nginx/html
RUN sed -i "s/flag{flag_placeholder}/'$flag'/" /usr/share/nginx/html/admintools/flag.txt
EXPOSE 80
