from flask import Flask, render_template
import yaml
import logging

app = Flask(__name__)

config = None
try:
    f = open('../config.yml', 'r')
    config = yaml.load(f, Loader=yaml.SafeLoader)
except OSError:
    logging.critical("Cannot load config file")
    exit(0)

@app.route('/')
def index():
    return 'It works'