
FROM python:3.10-slim

WORKDIR /app
RUN chmod -R 777 /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9090
CMD ["python", "web.py"]
