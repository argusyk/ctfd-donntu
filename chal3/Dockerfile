FROM nginx:stable-alpine
ARG flag='flag{javascript_is_cool}'

COPY src/ /usr/share/nginx/html
RUN flag_base64=$(echo $flaf | base64) && \
  sed -i 's/flag_placeholder_in_base64/'$flag_base64'/' /usr/share/nginx/html/challenge.js
EXPOSE 80
