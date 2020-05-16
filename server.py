#!/usr/bin/env python3

import os
import argparse
import json
import random
from configparser import ConfigParser
from parrot.driver import installer
from pathlib import Path

parser = argparse.ArgumentParser(description='Start the server')
parser.add_argument('--config', action='store', default=str(installer.getConfig()), help=f'location where the config.ini can be found (default: {installer.getConfig()})')
args = parser.parse_args()
config = ConfigParser()
config.read(args.config)

from flask import Flask
from flask.json import jsonify
from parrot.driver.mcrcon import MCRCON
from parrot import parser
with open(Path(__file__).parent / 'species.json') as f:
  SPECIES_LIST = json.load(f)

app = Flask(__name__)
driver = MCRCON(
  host=config["MCRCON"]["MCRCON_HOST"],
  port=config["MCRCON"]["MCRCON_PORT"],
  passwd=config["MCRCON"]["MCRCON_PASS"]
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

if __name__ == '__main__':
  app.run()