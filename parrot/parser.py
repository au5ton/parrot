
import re
import string

'''
There are 0 of a max 20 players online:
There are 1 of a max 20 players online: auston
There are 2 of a max 20 players online: auston, valleytoro
'''
def listPlayers(raw: str):
  x = raw.split(' ')
  x.reverse()
  for i in range(0, len(x)):
    if x[i].find(':') != -1:
      break
  # retrieve elements before the one containing the ':' colon
  players = x[:i]
  # remove punctuation
  players = [re.sub(r'[^\w\s]','',p) for p in players]
  return players

'''
There are 0 of a max 20 players online:
There are 1 of a max 20 players online: auston
There are 2 of a max 20 players online: auston, valleytoro
'''
def listSlots(raw: str):
  return {
    "online": int(raw.split(' ')[2]),
    "capacity": int(raw.split(' ')[6])
  }