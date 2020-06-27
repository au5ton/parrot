
from subprocess import check_output, PIPE
import re

# definitely a security concern, let's hope Minecraft doesn't send us back naughty things
def eval(code: str):
  stdout = check_output(["node"], input=code.encode())
  return stdout.decode('utf-8').strip()
