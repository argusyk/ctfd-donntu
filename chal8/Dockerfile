FROM python:3.10-slim

ARG flag="flag{access_granted}"

WORKDIR /app

COPY src/ .
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "$flag" > flag.txt

EXPOSE 5000

CMD ["python", "app.py"]
