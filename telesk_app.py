import os
import sys
from src.telesk import Telesk
from src.main.controller import controller
from src.main.model import initialize_db
from src.resources import get_commands
import logging.config
import json

if len(sys.argv) > 1 and sys.argv[1] == 'dev':
    logging.config.dictConfig(json.load(open('./logger.main.dev.json')))
else:
    logging.config.dictConfig(json.load(open('./logger.local.json')))

app = Telesk()
app.config['api_key'] = os.getenv('tele_key')
app.config['commands'] = get_commands()
app.config['allow_group'] = False
app.register_blueprint(controller)

if __name__ == '__main__':
    initialize_db()
    app.poll()
