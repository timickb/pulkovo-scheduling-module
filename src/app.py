from flask import Flask, render_template
from src.engine.parser import Parser
import logging
import sys
import getopt
import xlrd
import yaml

LOGGING_FORMAT = '[%(levelname)s] [%(asctime)-5s] %(message)s'

config = None
try:
    f = open('../config.yml', 'r')
    config = yaml.load(f, Loader=yaml.SafeLoader)
except OSError:
    logging.critical("Cannot load config file")
    exit(0)

year_plan = None
parser = Parser(config)

webserver = Flask(__name__, template_folder='./web/templates')

@webserver.route('/')
def index():
    if year_plan == None:
        year_plan = parser.parse_year_plan()
    return render_template('yearplan.html', data=year_plan, groups_amount=len(year_plan))

if __name__ == "__main__":
    logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
    logger = logging.getLogger()

    logger.info("Starting module")

    webserver.run(host='0.0.0.0', port=config['web_server_port'], debug=True)

    