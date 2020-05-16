#!/usr/bin/env python3

import os
import argparse
from configparser import ConfigParser
from parrot.driver import installer

parser = argparse.ArgumentParser(description='Start the server')
parser.add_argument('--config', action='store', default=str(installer.getConfig()), help=f'location where the config.ini can be found (default: {installer.getConfig()})')
args = parser.parse_args()
config = ConfigParser()
config.read(args.config)

from flask import Flask
from parrot.driver.mcrcon import MCRCON

app = Flask(__name__)
driver = MCRCON(
  host=config["MCRCON"]["MCRCON_HOST"],
  port=config["MCRCON"]["MCRCON_PORT"],
  passwd=config["MCRCON"]["MCRCON_PASS"]
  )

@app.route('/')
def hello_world():
  return driver.rawcmd('list')

if __name__ == '__main__':
  app.run()