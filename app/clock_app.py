import logging
import os

from flask import Flask, render_template
from waitress import serve

from utils import set_config_logging, get_actual_time

"""

HOST: 0.0.0.0
PORT: 8080

"""

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
    logging.warning("WEB PORT is None using default value: 8080")
    return 8080

  return web_port


def get_host_port() -> str:
  web_host = os.environ.get("WEB_HOST")
  
  if web_host is None:
    logging.warning("WEB HOST is None using default value: 0.0.0.0")
    return "0.0.0.0"

  return web_host


if __name__ == "__main__":
  set_config_logging()
  web_port = get_web_port()
  host_port = get_host_port()
  serve(app, host=host_port, port=web_port)
  

