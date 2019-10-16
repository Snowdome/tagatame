# tower.py last updated 08/10/2019

#  -------------------------Import Modules-------------------------
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
mobius = "mobius.png"
towerStart = "towerStart.png"
restore = "restore.png"
cfnRestore = Pattern("cfnRestore.png").targetOffset(100,180)
invalid = Pattern("invalid.png").targetOffset(0,240)
reward = Pattern("reward.png").targetOffset(0,160)


#Team
#s = selected team
tT1s = "tT1s.png"
tT2s = Pattern("tT2s.png").exact()
tT3s = Pattern("tT3s.png").exact()
tT4s = Pattern("tT4s.png").exact()
tT5s = Pattern("tT5s.png").exact()
tT6s = Pattern("tT6s.png").exact()
tT7s = Pattern("tT7s.png").exact()

# Select team (9+, Tower)
def slot9():
	sysMsg("Changing team")
	click(teamArrow)
	sleep(normal)
	click(teamNext)
	click(slot3)
	sysMsg("Team changed")



#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(type):
	if not exists(towerStart, 0):
		sysMsg("Going to selected tower (start floor menu)")
		if not exists(type):
			if exists(home, 0):
				clkIco(home)
			clkIco(quest, None, True)
			clkIco(challenge, None, True)
			clkIco(tower, None, True)
		# In case there are more towers
		# while not exists(type, short):
			# click(questArrow)
			# sysMsg("Turning page: tower")
		clkIco(type)
		clkIco(towerStart)
	else:
		sysMsg("Already in selected tower (start floor menu)")


# Choose team to enter tower and toggle auto (if not already on)
def autoTower(tower, team):
	i = 0
	sysMsg("Initializing AutoTower command")
	if not exists(btStart, 0):
		gotoTower(tower)
		
	while not exists(invalid):
		click(btStart)
		if exists(invalid, normal):
			clkIco(invalid)
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
				clkIco(reward)
				esc(questEnd)
				sleep(changePage)
				clkIco(towerStart)
			else:
				sysMsg("Returned to Battle Preparation")
				sleep(changePage)

def resTower():
	sysMsg("Checking for free restore")
	if exists(restore):
		clkIco(restore)
		clkIco(cfnRestore)
		sysMsg("All unit restored")
	else:
		sysMsg("Free restore is not available")

#  -------------------------Variables-------------------------



#  -------------------------Command-------------------------
#autoTower(thunder, tT1)
#resTower()
#autoTower(thunder, tT1)
#autoTower(veda, tT1)

#slot9()