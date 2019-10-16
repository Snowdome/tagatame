# tagatame.py last updated 13/10/2019

#  -------------------------Import Modules and Class-------------------------
from sikuli import *
import time
from inspect import currentframe, getframeinfo
import os


# Define class for story quest
class storyQ(object):
	def __init__(self, type, chapter, subChapter, stage):
		self.type = type	#main, seiseki, babel
		self.chapter = chapter
		self.subChapter = subChapter	#applicable to mainStory only
		self.stage = stage

class slot(int):
	def __init__(self, number, position):
		self.number = number
		self.position = position

#  -------------------------Settings-------------------------
#Settings.MinSimilarity = 0.8


# Waiting time
short = 0.1
normal = 1
double = 2
changePage = 5
extend = 7
long = 180
wTime = FOREVER



#  -------------------------Assets-------------------------
# External
fiddler = "fiddler.png"


# Homepage
home = "home.png"
settings = "settings.png"
mainMenu = "mainMenu.png"
quest = "quest.png"
SP = Pattern("mainMenu.png").targetOffset(-270,350)	# Location of Special Quest in respect to main men button
SPX = Pattern("mainMenu.png").targetOffset(-365,470)	# Location of Special Quest (type 2) in respect to main men button
questArrow = Pattern("mainMenu.png").targetOffset(-180,495)	# Location of down arrow in respect to main menu button
missionNew = "missionNew.png"
rewardGet = "rewardGet.png"


# Battle menu

noQuota = "noQuota.png"
noAP = "noAP.png"
leaf60 = "leaf60.png"
leaf120 = "leaf120.png"
leaf614 = "leaf614.png"
okAP = "okAP.png"
restoredAP = Pattern("restoredAP.png").targetOffset(0,215)	# Location of OK button in respect to the message
teamArrow = "teamArrow.png"
btStart = "btStart.png"
back = "back.png"


# Team slot (slot 8 not applicable to tower)
# Story and event team list stored separately
# Event includes Seiseki & Babel

slot1 = Pattern("teamArrow.png").targetOffset(70,56)	# Offset(70,56)
slot2 = Pattern("teamArrow.png").targetOffset(70,102)	# Offset(70,102)
slot3 = Pattern("teamArrow.png").targetOffset(70,148)	# Offset(70,148)
slot4 = Pattern("teamArrow.png").targetOffset(70,194)	# Offset(70,194)
slot5 = Pattern("teamArrow.png").targetOffset(70,240)	# Offset(70,240)
slot6 = Pattern("teamArrow.png").targetOffset(70,286)	# Offset(70,286)
slot7 = Pattern("teamArrow.png").targetOffset(70,332)	# Offset(70,332)
slot8 = Pattern("teamArrow.png").targetOffset(70,378)	# Offset(70,378)
teamNext = Pattern("teamArrow.png").targetOffset(170,340)	# Offset(170,340)

# Battle
birdView = "birdView.png"
toggleAuto = "toggleAuto.png"
autoOn = "autoOn.png"
btMenu = "btMenu.png"
quitQuest = "quitQuest.png"
btAgain = "btAgain.png"
confirm = "confirm.png"
btNext = "btNext.png"
questMission = "questMission.png"
visionMax = Pattern("visionMax.png").targetOffset(0,440)	# Location of OK button in respect to the title bar
questEnd = "questEnd.png"

shop = Pattern("shop.png").targetOffset(-85,210)



#  -------------------------Define Function-------------------------
# Debug message
def sysMsg(text):
	now = time.localtime()
	print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + text)


# Click icon (optional: delay = length // loop = repeat until no longer exists)
def clkIco(icon, delay=None, loop=False):
	if not exists(icon):
		sysMsg("Waiting for " + str(icon))
		wait(icon, wTime)
	if delay != None:
		sysMsg("Delay clicking on " + str(icon) + " for " + str(delay))
		sleep(delay)
	if loop == False:
		click(icon)
		sysMsg("Clicked on " + str(icon))
	else:
		try:
			click(icon)
			sleep(normal)
			sysMsg("Repeat clicking on " + str(icon))
		except FindFailed:
			sysMsg("Cannot find icon")


# Wait for icon and press ESC (optional: delay = length)
def esc(icon, length=None):
	if not exists(icon, normal):
		wait(icon, FOREVER)
		sysMsg("Waiting for " + str(icon))
	if length is not None:
		sleep(length)
		sysMsg("Delay pressing ESC for " + str(icon) + " for length = " + str(length))
	type(Key.ESC)
	sysMsg("Pressed ESC for " + str(icon))
	sleep(normal)


# Restore AP (optional: icon = leaf type)
def resAP(icon=leaf120):
	if exists(noAP):
		clkIco(icon)
		clkIco(okAP)
		clkIco(restoredAP)
	else:
		sysMsg("Invalid command - no insufficient AP message")

# After entering battle, toggle Auto if not On, and complete.
def btAction():
	wait(btMenu, 20)
	if exists(toggleAuto, normal):
		click(toggleAuto)
		sysMsg("Toggled auto")
		sleep(short)
	else:
		sysMsg("Auto already on")
	clkIco(questMission)
	sysMsg("Quest completed")
	while exists(visionMax):
		sysMsg("Vision achieved")
		sleep(normal)
		esc(visionMax)
	else:	
		sleep(changePage)
		type(Key.ESC)


# After entering battle, quit.
def btQuit():
	click(btMenu)
	click(quitQuest)
	click(confirm)


# Select team (1 - 8)
def teamSelect(slot):
	sysMsg("Changing team")
	click(teamArrow)
	sleep(normal)
	click(slot)
	sysMsg("Team changed")



# Get reward from completed mission
def getReward():
	clkIco(mainMenu)
	clkIco(missionNew)
	while exists(rewardGet):
		clkIco(rewardGet, None, True)
		sleep(normal)
		type(key.ESC)
	sysMsg("Done")

sysMsg("Imported tagatame.sikuli")