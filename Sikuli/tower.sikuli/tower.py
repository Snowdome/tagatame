# tower.py last updated 04/11/2019

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

# Define class for tower event and title bar
class tEvent():
	def __init__(self, logo, stage):
		self.logo = logo
		self.stage = stage

#  -------------------------Assets-------------------------
#Interface
challenge = "challenge.png"
tower = "tower.png"
veda = tEvent("vedaLogo.png", "vedaStage.png")
extra = tEvent("extraLogo.png", "dummy")
thunder = tEvent("thunderLogo.png", "dummy")
water = tEvent("waterLogo.png", "waterStage.png")
mobius = tEvent("mobiusLogo.png", "dummy")
towerStart = "towerStart.png"
restore = Pattern("restore.png").similar(0.95)
cfnRestore = Pattern("cfnRestore.png").targetOffset(100,180)	# Location in rspect to the message
unitRestored = Pattern("unitRestored.png").targetOffset(0,295)	# Location of OK button in respect to the title bar
invalid = Pattern("invalid.png").targetOffset(0,240)	# Location in rspect to the message
teamEmpty = Pattern("teamEmpty.png").targetOffset(100,130)	# Location of confirm button in respect to the message
reward = Pattern("reward.png").targetOffset(0,160)	# Location in rspect to the message



# -------------------------Variables-------------------------
# Refer to tagatame.py for class.team
team1 = team(slot1, 1)
team2 = team(slot2, 1)
team3 = team(slot3, 1)
team4 = team(slot4, 1)
team5 = team(slot5, 1)
team6 = team(slot6, 1)
team7 = team(slot7, 1)
team8 = team("team8.png", 2)
team9 = team("team9.png", 2)
team10 = team("team10.png", 2)

#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(tEvent):
	if not exists(towerStart, short):
		sysMsg("Going to selected tower (floor selection menu)")
		if not exists(tEvent.logo, short):
			if exists(home, short):
				clkObj(home)
			clkObj(quest, 0, 1)
			clkObj(challenge, 0, 1)
			clkObj(tower, 0, 1)
		# In case there are more towers
		# while not exists(tEvent.logo, short):
			# click(questArrow)
			# sysMsg("Turning page: tower")
		clkObj(tEvent.logo)
	else:
		sysMsg("Challenge button found. Checking tower type.")
		if tEvent.stage == "dummy":
			sysMsg("Warning - Tower title has not been recorded. Proceed with the current tower.")
		else:
			if exists(tEvent.stage, 0):
				sysMsg("Already in selected tower (floor selection menu)")
			else:
				sysMsg("In the wrong tower. Moving to the selected tower.")
				clkObj(back)
				# In case there are more towers
				# while not exists(tEvent.logo, short):
					# click(questArrow)
					# sysMsg("Turning page: tower")
				clkObj(tEvent.logo)
	clkObj(towerStart)

# Choose team to enter tower and toggle auto (if not already on)
# Tower: Page 1 [1-7] // Page 2 [8-12] // Page 3 [13-16] // Page 4 [17-20]
def autoTower(tEvent, team):
	i = 0
	sysMsg("Initializing AutoTower command")
	if not exists(btStart, short):
		gotoTower(tEvent)
	else:
		sysMsg("Battle Start button found")
	teamSelect(team.position, team.page)
	while i != -1:
		click(btStart)
		if exists(invalid, normal):
			clkObj(invalid, 0, 0, "Invalid")
			i = -1
			sysMsg("*************** Invalid team composition, end of command ***************")
		else:	
			if exists(teamEmpty, 0):
				sysMsg("Reminder - Team consists of empty slot")
				clkObj(teamEmpty)	
			wait(btMenu, long)
			if exists(toggleAuto, normal):
				click(toggleAuto)
				sysMsg("Toggled auto")
				sleep(short)
			else:
				sysMsg("Auto already on")
			t = 0
			while t != -1:
				if exists(home, 0):
					sysMsg("Returned to Battle Preparation")
					sleep(changePage)
					t = -1
					i = -1
				else:
					if exists(reward, 0):
						i = i + 1
						sysMsg("*************** " + str(i) + " floor(s) cleared ***************")
						clkObj(reward, 0, 0, "Reward")
						clkObj(btEnd, 0, 1)
						sleep(changePage)
						clkObj(towerStart)
						t = -1
					else:
						t = t + 10	
						sleep(10)
						sysMsg("Completion not found. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")
		sysMsg("End of command")



def resTower():
	sysMsg("Checking for free restore")
	if exists(btStart, 0):
		clkObj(back)
	if exists(restore):
		clkObj(restore)
		clkObj(cfnRestore, 0, 0, "Confirm Restore")
		sysMsg("*************** All units have been restored ***************")
		clkObj(unitRestored)
	else:
		sysMsg("*************** Free restore is not available ***************")


#  -------------------------Command-------------------------
# Seasonal Tower
#autoTower(water, team9)
#autoTower(water, team10)
#autoTower(water, team2)
#autoTower(water, team8)
#autoTower(water, team1)
#autoTower(water, team3)
#autoTower(water, team4)
#autoTower(water, team5)
#autoTower(water, team6)
#autoTower(water, team7)
#resTower()

# Ordinary Tower
autoTower(veda, team8)
autoTower(veda, team2)
autoTower(veda, team3)
autoTower(veda, team4)
autoTower(veda, team5)
autoTower(veda, team1)
autoTower(veda, team6)
autoTower(veda, team7)
resTower()