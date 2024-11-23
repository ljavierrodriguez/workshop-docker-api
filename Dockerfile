FROM python:3.12-slim

WORKDIR /api

COPY . /api

RUN pip3 install --no-cache-dir -r /api/requirements.txt

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8100

EXPOSE 8100

CMD ["flask", "run", "--host=0.0.0.0", "--port=8100"]