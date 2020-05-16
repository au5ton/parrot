from flask import Flask
from parrot.driver.mcrcon import MCRCON

app = Flask(__name__)
driver = MCRCON(passwd='test')

@app.route('/')
def hello_world():
  return driver.rawcmd('list')

if __name__ == '__main__':
  app.run()