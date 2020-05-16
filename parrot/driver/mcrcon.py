
from parrot.driver import installer
from subprocess import check_output
import re


# See: https://stackoverflow.com/a/19016117
# def remove_control_characters(s):
#     return "".join(ch for ch in s if unicodedata.category(ch)[0]!="C")

# See: https://www.w3resource.com/python-exercises/re/python-re-exercise-45.php
def remove_control_characters(s):
  reaesc = re.compile(r'\x1b[^m]*m')
  return reaesc.sub('', s)

if not installer.checkExists():
  installer.install()


class MCRCON:
  # password cannot be empty
  def __init__(self, passwd, host='127.0.0.1', port=25575):
    self.host = host
    self.port = port
    self.passwd = passwd
    self.bin = installer.getBinary()

  def rawcmd(self, command) -> str:
    stdout = check_output([
      self.bin, '-H', self.host, '-P', str(self.port), '-p', self.passwd, command
      ])
    return remove_control_characters(stdout.decode('utf-8')).strip()

  def test(self):
    print(f'Hello, {self.host}!')
    print(self.bin)
    print(check_output([self.bin, '-h']).decode('utf-8'))

