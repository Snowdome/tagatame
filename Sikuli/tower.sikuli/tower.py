# tower.py last updated 12/09/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

# Define class for tower event and title bar
class tEvent():
	def __init__(self, name, logo, stage, stageSmall):
		self.name = name
		self.logo = logo
		self.stage = stage
		self.stageSmall = stageSmall
	def __repr__(self):
		return self.name

#  -------------------------Assets-------------------------
#Interface
tower = "tower.png"
towerTitle = "towerTitle.png"
veda = tEvent("veda", "vedaLogo.png", "vedaStage.png", Pattern("vedaStage2.png").similar(0.90))
extra = tEvent("extra", "extraLogo.png", "dummy", "dummy")
fire = tEvent("fire", Pattern("fireLogo.png").exact(), Pattern("fireStage.png").similar(0.90), Pattern("fireStage2.png").similar(0.90))
water = tEvent("water", Pattern("waterLogo.png").exact(), Pattern("waterStage.png").similar(0.90), Pattern("waterStage2.png").similar(0.90))
thunder = tEvent("thunder", Pattern("thunderLogo.png").exact(), Pattern("thunderStage.png").similar(0.90), Pattern("thunderStage2.png").similar(0.90))
wind = tEvent("wind", Pattern("windLogo.png").exact(), Pattern("windStage.png").similar(0.90), Pattern("windStage2.png").similar(0.90))
light = tEvent("light", Pattern("lightLogo.png").exact(), Pattern("lightStage.png").similar(0.90), Pattern("lightStage2.png").similar(0.90))
dark = tEvent("dark", Pattern("darkLogo.png").exact(), Pattern("darkStage.png").similar(0.90), Pattern("darkStage2.png").similar(0.90))
mobius = tEvent("mobius", "mobiusLogo.png", "dummy", "dummy")
currentFloor = "currentFloor.png"
towerStart = "towerStart.png"
towerRestart = "towerRestart.png"
restore = Pattern("restore.png").similar(0.95)
cfnRestore = Pattern("cfnRestore.png").targetOffset(100,225)	# Location in rspect to the message
unitRestored = Pattern("unitRestored.png").targetOffset(0,295)	# Location of OK button in respect to the title bar
invalid = Pattern("invalid.png").targetOffset(0,240)	# Location in rspect to the message
teamEmpty = Pattern("teamEmpty.png").targetOffset(100,130)	# Location of confirm button in respect to the message
reward = Pattern("reward.png").targetOffset(0,160)	# Location in rspect to the message
towerComplete = Pattern("towerComplete.png").targetOffset(-145,345)	# Location of OK button in respect to the message



# -------------------------Variables-------------------------
# Refer to tagatame.py for class.team
team1 = team("team1", slot1, 1)
team2 = team("team2", slot2, 1)
team3 = team("team3", slot3, 1)
team4 = team("team4", slot4, 1)
team5 = team("team5", slot5, 1)
team6 = team("team6", slot6, 1)
team7 = team("team7", slot7, 1)
team8 = team("team8", "team8.png", 2)
team9 = team("team9", "team9.png", 2)
team10 = team("team10", "team10.png", 2)

#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(tEvent):
	if not exists(towerStart, short):
		if not exists(towerTitle, short):
			sysMsg("Going to selected tower.")
			if not exists(tEvent.logo, short):
				if exists(home, short):
					clkObj(home)
					sleep(normal)
				if exists(invalid, 0):
					clkObj(invalid, 0, 0, "Invalid")
				clkObj(quest, 0, challenge)
				clkObj(challenge, 0, tower)
				clkObj(tower, 0, 1)
				waitObj(towerTitle, 10)
			else:
				sysMsg("Tower title menu found. Choosing selected tower.")
		while not exists(tEvent.logo, short):
			click(questArrow)
			sysMsg("Turning page: tower")
			sleep(normal)
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
				clkObj(back, loop=towerTitle)
				while not exists(tEvent.logo, short):
					click(questArrow)
					sysMsg("Turning page: tower")
					sleep(normal)
				clkObj(tEvent.logo)
	waitObj(currentFloor, 15)
	if exists(towerRestart, 0):
		sysMsg("Error - Tower is already cleared")
	else:
		clkObj(towerStart)

# Choose team to enter tower and toggle auto (if not already on)
# Tower: Page 1 [1-7] // Page 2 [8-12] // Page 3 [13-16] // Page 4 [17-20]
def autoTower(tEvent, team):
	i = 0
	sysMsg("Initializing AutoTower command: " + repr(tEvent) + ", " + repr(team))
	if exists(towerRestart, 0):
		if exists(tEvent.stage, 0):
			sysMsg("Error - Tower is already cleared")
	else:		
		if not exists(btStart, short):
			gotoTower(tEvent)
			if not exists(towerRestart, 0):
				teamSelect(team.position, team.page)
			else:
				i = -1
		else:
			if tEvent.stageSmall == "dummy":
				popAsk("Battle Start button found, proceed with current setup?", "Waiting for decision")
				if not decision:
					sysMsg("No button has been pressed. Returning to home screen.")
					clkObj(home)
					gotoTower(tEvent)
					teamSelect(team.position, team.page)
				else:
					sysMsg("Yes button has been pressed. Engaging battle.")
			else:
				if not exists(tEvent.stageSmall):
					sysMsg("In the wrong tower. Moving to the selected tower.")
					clkObj(home)
					gotoTower(tEvent)
					teamSelect(team.position, team.page)
				else:
					sysMsg("Already in the selected tower.")
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
				waitObj(btMenu, 180)
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
							if exists(towerComplete, 0):
								sysMsg("*************** Tower cleared ***************")
								clkObj(towerComplete, 0, 1, "Congratulations OK")
								t = -1
								i = -1
								waitObj(towerRestart, 30)
								sysMsg("*************** End of command ***************")
							else:
								clkObj(towerStart)
								t = -1
						else:
							t = t + 10
							sleep(10)
							sysMsg("Completion message not found. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")



def resTower():
	sysMsg("Checking for free restore")
	if exists(towerRestart, 0):
		sysMsg("Error - Tower is already cleared")
	else:
		if exists(btStart, 0):
			clkObj(back)
		if exists(restore):
			clkObj(restore)
			clkObj(cfnRestore, 0, 0, "Confirm Restore")
			sysMsg("*************** All units have been restored ***************")
			clkObj(unitRestored)
		else:
			sysMsg("*************** Free restore is not available ***************")

def autoTowerVeda():
	#Ordinary Tower
	autoTower(veda, team1)
	autoTower(veda, team2)
	autoTower(veda, team3)
	autoTower(veda, team4)
	autoTower(veda, team5)
	autoTower(veda, team6)
	autoTower(veda, team7)
	resTower()
	autoTower(veda, team1)
	autoTower(veda, team2)
	autoTower(veda, team3)
	autoTower(veda, team4)
	autoTower(veda, team5)
	autoTower(veda, team6)
	autoTower(veda, team7)

def autoTowerType():
	# Seasonal Tower
	autoTower(wind, team1)
	autoTower(wind, team2)
	autoTower(wind, team3)
	autoTower(wind, team4)
	autoTower(wind, team5)
	autoTower(wind, team6)
	autoTower(wind, team7)
	resTower()
	autoTower(wind, team1)
	autoTower(wind, team2)
	autoTower(wind, team3)
	autoTower(wind, team4)
	autoTower(wind, team5)
	autoTower(wind, team6)
	autoTower(wind, team7)
	
	autoTower(light, team1)
	autoTower(light, team2)
	autoTower(light, team3)
	autoTower(light, team4)
	autoTower(light, team5)
	autoTower(light, team6)
	autoTower(light, team7)
	resTower()
	autoTower(light, team1)
	autoTower(light, team2)
	autoTower(light, team3)
	autoTower(light, team4)
	autoTower(light, team5)
	autoTower(light, team6)
	autoTower(light, team7)
	
	autoTower(dark, team1)
	autoTower(dark, team2)
	autoTower(dark, team3)
	autoTower(dark, team4)
	autoTower(dark, team5)
	autoTower(dark, team6)
	autoTower(dark, team7)
	resTower()
	autoTower(dark, team1)
	autoTower(dark, team2)
	autoTower(dark, team3)
	autoTower(dark, team4)
	autoTower(dark, team5)
	autoTower(dark, team6)
	autoTower(dark, team7)

#  -------------------------Command-------------------------
autoTowerVeda()