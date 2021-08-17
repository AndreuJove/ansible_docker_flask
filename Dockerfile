FROM python:3.8-slim-buster

ENV WEB_PORT=80
ENV WEB_HOST="0.0.0.0"

RUN python3 -m venv /opt/venv

# Install dependencies:
COPY requirements.txt .
RUN .. /opt/venv/bin/activate && pip install -r requirements.txt

# Run the application:
RUN mkdir project
COPY ../ /project
CMD .. /opt/venv/bin/activate && exec python project/app/clock_app.py