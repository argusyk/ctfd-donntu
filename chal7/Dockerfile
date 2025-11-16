FROM python:3.10-slim

ARG flag="flag{ecb_aes_s3cret}"

WORKDIR /app

COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "$flag" > flag.txt

EXPOSE 5000

CMD ["python", "app.py"]
