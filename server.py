#!/usr/bin/env python3

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # this is so ghetto but python is weird about these things
import json
import random
from configparser import ConfigParser
from parrot.driver import installer
from pathlib import Path

config = ConfigParser()
enough_env_vars_given = True


if 'MCRCON_HOST' not in os.environ or 'MCRCON_PORT' not in os.environ or 'MCRCON_PASS' not in os.environ:
  print('Some environment variables are missing. A config file will be used to provide these values.')
  enough_env_vars_given = False

if len(config.read(installer.getConfig())) == 0 and enough_env_vars_given == False:
  print(f'A config.ini file could not be read from {installer.getConfig()}')
  exit(1)

from flask import Flask
from flask.json import jsonify
from parrot.driver.mcrcon import MCRCON
from parrot import parser
with open(Path(__file__).parent / 'species.json') as f:
  SPECIES_LIST = json.load(f)

app = Flask(__name__)
driver = MCRCON(
  host=os.environ.get('MCRCON_HOST') if 'MCRCON_HOST' in os.environ else config["MCRCON"]["MCRCON_HOST"],
  port=os.environ.get('MCRCON_PORT') if 'MCRCON_PORT' in os.environ else config["MCRCON"]["MCRCON_PORT"],
  passwd=os.environ.get('MCRCON_PASS') if 'MCRCON_PASS' in os.environ else config["MCRCON"]["MCRCON_PASS"]
  )

@app.route('/')
def index():
  return f'Hello, {random.choice(SPECIES_LIST)}!'

@app.route('/api/cmd/<command>')
def cmd(command):
  return jsonify(driver.rawcmd(command))

@app.route('/api/list')
def listp():
  return jsonify(parser.listPlayers(driver.rawcmd('list')))

@app.route('/api/slots')
def slots():
  return jsonify(parser.listSlots(driver.rawcmd('list')))

@app.route('/api/player/<player>')
def player(player):
  return jsonify(json.loads(parser.dataGetEntity(driver.rawcmd(f'data get entity @p[name={player}]'))))

if __name__ == '__main__':
  app.run(host='0.0.0.0')