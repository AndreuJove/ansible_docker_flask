import logging
import os

from flask import Flask, render_template
from waitress import serve

from utils import set_config_logging, get_actual_time

app = Flask(__name__)

@app.route("/clock")
def clock_endpoint() -> str:
  return get_actual_time()


@app.route("/")
def home() -> str:
  return render_template("index.html")


def get_web_port() -> int:
  web_port = os.environ.get("WEB_PORT")

  if web_port is None:
    logging.warning("WEB PORT is None using default value: 80")
    return 80

  logging.info(f"Using ENV PORT: {web_port}")
  return int(web_port)


def get_host_port() -> str:
  web_host = os.environ.get("WEB_HOST")

  if web_host is None:
    logging.warning("WEB HOST is None using default value: 0.0.0.0")
    return "0.0.0.0"

  logging.info(f"Using ENV HOST: {web_host}")
  return web_host


if __name__ == "__main__":
  set_config_logging()
  web_port = get_web_port()
  web_host = get_host_port()
  serve(app, host=web_host, port=web_port)
  

