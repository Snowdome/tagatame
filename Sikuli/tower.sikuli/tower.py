# tower.py last updated 20/10/2019

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


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


#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(type):
	if not exists(towerStart, short):
		sysMsg("Going to selected tower (team preparation menu)")
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
		clkObj(towerStart)
	else:
		sysMsg("Already in selected tower (team preparation menu)")


# Choose team to enter tower and toggle auto (if not already on)
# Tower: Page 1 [1-7] // Page 2 [8-12] // Page 3 [13-16] // Page 4 [17-20]
def autoTower(tower, teamSlot, teamPage=1):
	i = 0
	sysMsg("Initializing AutoTower command")
	if not exists(btStart, short):
		gotoTower(tower)
		teamSelect(teamSlot, teamPage)
	while not exists(invalid):
		click(btStart)
		if exists(invalid, normal):
			clkObj(invalid)
			sysMsg("Invalid team composition")
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
				clkObj(Pattern("btEnd.png").targetOffset(50,0))
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
#autoTower(veda, slot1)
autoTower(veda, slot2)