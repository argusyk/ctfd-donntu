FROM php:7.3-apache

RUN apt-get update && \
    apt-get install -y logrotate cron
COPY apache_logrotate.conf /etc/logrotate.d/apache2
RUN echo "* * * * * root /usr/sbin/logrotate /etc/logrotate.conf" > /etc/crontab

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

COPY src/ /var/www/html/
CMD ["apache2-foreground"]
