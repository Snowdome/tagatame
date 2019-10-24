# tower.py last updated 21/10/2019

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


class team():
	def __init__(self, position, page):
		self.position = position
		self.page = page


#  -------------------------Assets-------------------------
#Interface
challenge = "challenge.png"
tower = "tower.png"
veda = "veda.png"
extra = "extra.png"
thunder = "thunder.png"
water = "water.png"
mobius = "mobius.png"
towerStart = "towerStart.png"
restore = "restore.png"
cfnRestore = Pattern("cfnRestore.png").targetOffset(100,180)
invalid = Pattern("invalid.png").targetOffset(0,240)
reward = Pattern("reward.png").targetOffset(0,160)



# -------------------------Variables-------------------------
team1 = team(slot1, 1)
team2 = team(slot2, 1)
team3 = team(slot3, 1)
team4 = team(slot4, 1)
team5 = team(slot5, 1)
team6 = team(slot6, 1)
team7 = team(slot7, 1)
team8 = team("team8.png", 2)
team9 = team("team9.png", 2)

#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(type):
	if not exists(towerStart, short):
		sysMsg("Going to selected tower (floor selection menu)")
		if not exists(type, short):
			if exists(home, short):
				clkObj(home)
			clkObj(quest, 0, 1)
			clkObj(challenge, 0, 1)
			clkObj(tower, 0, 1)
		# In case there are more towers
		# while not exists(type, short):
			# click(questArrow)
			# sysMsg("Turning page: tower")
		clkObj(type)
	else:
		sysMsg("Already in selected tower (floor selection menu)")
	clkObj(towerStart)

# Choose team to enter tower and toggle auto (if not already on)
# Tower: Page 1 [1-7] // Page 2 [8-12] // Page 3 [13-16] // Page 4 [17-20]
def autoTower(tower, team, teamPage=1):
	i = 0
	sysMsg("Initializing AutoTower command")
	if not exists(btStart, short):
		gotoTower(tower)
	else:
		sysMsg("Battle Start button found")
	teamSelect(team.position, team.page)
	while not exists(invalid):
		click(btStart)
		if exists(invalid, normal):
			clkObj(invalid)
			sysMsg("Invalid team composition, end of function")
		else:	
			wait(btMenu, 20)
			if exists(toggleAuto, normal):
				click(toggleAuto)
				sysMsg("Toggled auto")
				sleep(short)
			else:
				sysMsg("Auto already on")
			wait(reward or towerStart, FOREVER)
			if exists(reward):
				i = i + 1
				sysMsg("***************" + str(i) + " floor(s) cleared***************")
				clkObj(reward)
				clkObj(btEnd)
				sleep(normal)
				mouseMove(50,0)
				click(atMouse())
				sleep(changePage)
				clkObj(towerStart)
			else:
				sysMsg("Returned to Battle Preparation")
				sleep(changePage)

def resTower():
	sysMsg("Checking for free restore")
	if exists(restore):
		clkObj(restore)
		clkObj(cfnRestore)
		sysMsg("All unit restored")
	else:
		sysMsg("Free restore is not available")


#  -------------------------Command-------------------------
#autoTower(thunder, tT1)
#resTower()
#autoTower(thunder, tT1)
autoTower(veda, team8)
autoTower(veda, team2)
autoTower(veda, team3)
autoTower(veda, team4)
autoTower(veda, team5)
autoTower(veda, team1)
autoTower(veda, team6)
autoTower(veda, team7)
