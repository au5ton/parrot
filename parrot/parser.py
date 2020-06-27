
import re
import json
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

'''
auston has the following entity data: {Brain: {memories: {}}, HurtByTimestamp: 0, SleepTimer: 0s, Attributes: [{Base: 0.10000000149011612d, Name: \"minecraft:generic.movement_speed\"}], Invulnerable: 0b, FallFlying: 0b, PortalCooldown: 0, AbsorptionAmount: 0.0f, abilities: {invulnerable: 1b, mayfly: 1b, instabuild: 0b, walkSpeed: 0.1f, mayBuild: 0b, flying: 1b, flySpeed: 0.05f}, FallDistance: 0.0f, recipeBook: {recipes: [], isBlastingFurnaceFilteringCraftable: 0b, isSmokerGuiOpen: 0b, isFilteringCraftable: 0b, toBeDisplayed: [], isFurnaceGuiOpen: 0b, isGuiOpen: 0b, isFurnaceFilteringCraftable: 0b, isBlastingFurnaceGuiOpen: 0b, isSmokerFilteringCraftable: 0b}, DeathTime: 0s, XpSeed: -1762884102, XpTotal: 0, UUID: [I; 1577784142, -539867416, -1716572465, -495806708], playerGameType: 3, seenCredits: 0b, Motion: [0.0d, 0.0d, 0.0d], Health: 20.0f, foodSaturationLevel: 5.0f, Air: 300s, OnGround: 0b, Dimension: \"minecraft:overworld\", Rotation: [317.23154f, 17.453646f], XpLevel: 0, Score: 0, Pos: [191.21348004379465d, 75.42368787190134d, -16.258547900128978d], previousPlayerGameType: 2, Fire: 0s, XpP: 0.0f, EnderItems: [], DataVersion: 2567, foodLevel: 20, foodExhaustionLevel: 0.478f, HurtTime: 0s, SelectedItemSlot: 0, Inventory: [], foodTickTimer: 0}
'''
def dataGetEntity(raw: str):
  selector = ""
  if raw.find(selector) == -1:
    return "Error"
  else:
    return json.dumps(json.loads(raw[(raw.find(selector) + len(selector)):]))
