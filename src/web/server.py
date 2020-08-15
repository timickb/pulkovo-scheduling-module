from flask import Flask, render_template
from src.engine.parser import Parser
import yaml
import logging

def server():

    app = Flask(__name__, template_folder='./templates')

    config = None
    try:
        f = open('../config.yml', 'r')
        config = yaml.load(f, Loader=yaml.SafeLoader)
    except OSError:
        logging.critical("Cannot load config file")
        exit(0)

    year_plan = None
    parser = Parser(config)

    @app.route('/')
    def index():
        if year_plan == None:
            year_plan = parser.parse_year_plan()
        return render_template('yearplan.html', data=year_plan, groups_amount=len(year_plan))

    app.run(host='0.0.0.0', port=config['web_server_port'], debug=True)