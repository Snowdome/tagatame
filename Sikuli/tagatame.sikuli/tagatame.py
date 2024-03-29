# tagatame.py last updated 10/05/2021

#  -------------------------Import Modules and Classes-------------------------
from sikuli import *
import time
from inspect import currentframe, getframeinfo
import os


# Define class for team and page number
class team():
	def __init__(self, name, position, page):
		self.name = name
		self.position = position
		self.page = page
	def __repr__(self):
		return self.name

#  -------------------------Settings-------------------------
# Settings.MinSimilarity = 0.8

# Waiting time
short = 0.1
normal = 1
double = 2
changePage = 5
extend = 7
refresh = 10
long = 180
battle = 300
wTime = 10
msgError = "Error: n must be empty or positive"
msgEnd = "***************End of command***************"

#  -------------------------Assets-------------------------
# External
fiddler = "fiddler.png"


# Homepage
reFocus = Pattern("reFocus.png").targetOffset(-25,0)
home = "home.png"
settings = "settings.png"
mainMenu = "mainMenu.png"
questLoc = Pattern("openedMenu.png").targetOffset(-85,460)	# Location of quest button in respect to the opened menu button
quest = Pattern("mainMenu.png").targetOffset(-90,460)	# Location of quest button in respect to the menu button
story = "story.png"
event = "event.png"
eventQ = "eventQ.png"
daily = "daily.png"
archive = "archive.png"
archivePageDown = Pattern("mainMenu.png").targetOffset(-127,435)	# Location of quest button in respect to the menu button
eventTitle = "eventTitle.png"
challenge = "challenge.png"
questArrow = Pattern("mainMenu.png").targetOffset(-180,495)	# Location of down arrow in respect to main menu button
unit = "unit.png"

missionNew = "missionNew.png"
rewardGet = "rewardGet.png"
autoRepeat = "autoRepeat.png"
arComplete = Pattern("arComplete.png").similar(0.50)
arReward = "arReward.png"
arEnd = "arEnd.png"
okAR = "okAR.png"
arMenu = "arMenu.png"
arMax = Pattern("arMax.png").targetOffset(-200,0)
arRefillAP = Pattern("arRefillAP.png").targetOffset(-65,0)
arStart = "arStart.png"
playerReward = Pattern("playerReward.png").targetOffset(0,450)	# Loc of OK button in respect to the title bar
arReturn = "arReturn.png"
arReturnHome = "arReturnHome.png"

# Battle menu

noQuota = "noQuota.png"
noAR = "noAR.png"
noQuotaOK = "noQuotaOK.png"
noAP = "noAP.png"
noAPRDP = "noAPRDP.png"
leaf60 = "leaf60.png"
leaf60RDP = "leaf60RDP.png"
leaf120 = "leaf120.png"
leaf120RDP = "leaf120RDP.png"
leafAdd = "leafAdd.png"
leafAddRDP = "leafAddRDP.png"
okAP = Pattern("okAP.png").similar(0.85)
okAPRDP = "okAPRDP.png"
restoredAP = Pattern("restoreAP.png").similar(0.90).targetOffset(0,215)	# Location of OK button in respect to the message
restoredAPRDP = Pattern("restoredAPRDP.png").targetOffset(0,190) # Location of OK button in respect to the message
teamArrow = "teamArrow.png"
btStart = "btStart.png"
btAgain = "btAgain.png"
back = "back.png"
runeFull = Pattern("runeFull.png").targetOffset(5,227) # Location of OK button in respect to the message
disassembly = "disassembly.png"


# Team slot (slot 8 not applicable to tower)
# Story and event team list stored separately
# Event includes Seiseki & Babel

slot1 = Pattern("teamArrow.png").targetOffset(70,56)	# Offset(70,56)
slot2 = Pattern("teamArrow.png").targetOffset(70,102)	# Offset(70,102)
slot3 = Pattern("teamArrow.png").targetOffset(70,155)	# Offset(70,148)
slot4 = Pattern("teamArrow.png").targetOffset(70,205)	# Offset(70,194)
slot5 = Pattern("teamArrow.png").targetOffset(70,230)	# Offset(70,230)
slot6 = Pattern("teamArrow.png").targetOffset(70,280)	# Offset(70,280)
slot7 = Pattern("teamArrow.png").targetOffset(70,325)	# Offset(70,325)
slot8 = Pattern("teamArrow.png").targetOffset(70,378)	# Offset(70,378)
teamNext = Pattern("teamArrow.png").targetOffset(170,340)	# Offset(170,340)
teamEmpty = Pattern("teamEmpty.png").targetOffset(100,125)	# Location of confirm button in respect to the message

# Battle
birdView = "birdView.png"
toggleAuto = "toggleAuto.png"
autoOn = "autoOn.png"
btMenu = "btMenu.png"
quitQuest = "quitQuest.png"
escMenu = "escMenu.png"
btAgain = "btAgain.png"
confirm = "confirm.png"
cancel = "cancel.png"
btNext = "btNext.png"
questMission = Pattern("questMission.png").targetOffset(0,445)
visionMax = Pattern("visionMax.png").targetOffset(0,440)	# Location of OK button in respect to the title bar
btEnd = "btEnd.png"

peddlerShop = "peddlerShop.png"



#  -------------------------Define Function-------------------------
# Debug message
list = ("Retry", "Skip", "Terminate")
def sysMsg(msg, title=0, object=0):
	now = time.localtime()
	print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + msg)
	if title == "FindFailed Error (clkObj)":	# Sikilu pop up message
		r = 1
		while r != -1:
			decision = select("(" + str(r) + ")" + msg, title, options=list)
			now = time.localtime()
			if decision == list[0]:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Trying to locate the missing object again.")
				if exists(object, 0):
					now = time.localtime()
					click(object)
					print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Found and clicked the missing object.")
					r = -1
				else:
					now = time.localtime()
					print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Still cannot locate the missing object.")
					r = r + 1
					
			elif decision == list[1]:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[1] Proceed the current command with the missing object being skipped.")
				r = -1
			else:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[2] Terminatd the command.")
				exit(1)
	elif title == "FindFailed Error (waitObj)":
		r = 1
		while r != -1:
			decision = select("(" + str(r) + ")" + msg, title, options=list)
			now = time.localtime()
			if decision == list[0]:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Trying to locate the missing object again.")
				if exists(object, 0):
					now = time.localtime()
					print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Found the missing object.")
					r = -1
				else:
					now = time.localtime()
					print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[0] Still cannot locate the missing object.")
					r = r + 1
			elif decision == list[1]:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[1] Proceed the current command with the missing object being skipped.")
				r = -1
			else:
				print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "[2] Terminatd the command.")
				exit(1)

# Click object (optional: delay = length(sec), loop = 0/1/nextObject, remark = use customized message on log, ff = deccision on findFailed error)
def clkObj(object, delay=0, loop=0, remark=0, ff=0):
	if remark == 0:
		subject = repr(object)
	else:
		subject = remark
	try:
		if not exists(object):
			sysMsg("Waiting for " + subject)
			wait(object, wTime)
		if delay != 0:
			sysMsg("Delay clicking on " + subject + " for " + str(delay) + " sec")
			sleep(delay)
		if loop == 0:
			click(object)
			sysMsg("Clicked on " + subject)
		else:
			t = 0
			while t != -1:
				if exists(object, 0):
					click(object)
					mouseMove(10,0)
					sleep(1)
					sysMsg("Clicked on " + subject)
					if loop == 1:
						if exists(object, 0):
							t = t + 1
							sysMsg("Repeat clicking on " + subject + "; total looped time = " + str(t) + " times.")
						else:	
							t = -1
							sysMsg("Current object passed, loop completed.")
					else:
						if not exists(loop, 0):
							t = t + 1
							sysMsg("Cannot find " + repr(loop) + "; repeat clicking on " + subject + "; total looped time = " + str(t) + " sec.")
						else:
							t = -1
							sysMsg(repr(loop) + " found, loop completed.")
				else:
					sysMsg(subject + " no longer exists.")
					t = -1
	except FindFailed:
		if ff == "skip":
			sysMsg("Cannot find " + subject + ". Chosen: [1]Skip")
		else:
			sysMsg("Cannot find " + subject + ". Please choose: [0]Retry, [1]Skip, [2]Terminate", "FindFailed Error (clkObj)", object)

# Wait for object
def waitObj(object, time=wTime, remark=0, errMsg="N/A", ff=0):
	if remark == 0:
		subject = repr(object)
	else:
		subject = remark
	try:
		sysMsg("Waiting for " + subject + " for " + str(time))
		wait(object, time)
	except FindFailed:
		if ff == "skip":
			sysMsg("Cannot find " + subject + ". Chosen: [1]Skip")
		else:
			if errMsg == "N/A":
				sysMsg("Cannot find " + subject + ". Please choose: [0]Retry, [1]Skip, [2]Terminate", "FindFailed Error (waitObj)", object)
			else:
				sysMsg(message + "\nCannot find " + subject + ". Please choose: [0]Retry, [1]Skip, [2]Terminate", "FindFailed Error (waitObj)", object)

# Wait for object and press ESC (optional: delay = length(ms))
def esc(object, delay=0, loop=0, remark="N/A"):
	if remark == "N/A":
		subject = repr(object)
	else:
		if remark == 1:
			subject = object.remark
		else:
			subject = remark
	if not exists(object):
		sysMsg("Waiting for " + subject)
		wait(object, wTime)
	if delay != 0:
		sysMsg("Delay ESC for " + subject + " for " + str(delay))
		sleep(delay)
	if loop == 0:
		type(Key.ESC)
		sysMsg("ESC on " + subject)
	else:
		try:
			type(Key.ESC)
			sleep(normal)
			sysMsg("Repeat ESC on " + subject)
		except FindFailed:
			sysMsg("Cannot find object")


# AP Check (object = lastAction, optional: item = leaf type, quantity)
def apCheck(object, item=leaf120, q=1, nextObj="N/A"):
	if exists(noAP, normal):
		sysMsg("Insufficient AP.")
		clkObj(item)
		while q != 1:
			clkObj(leafAdd)
			q = q - 1
		clkObj(okAP)
		clkObj(restoredAP, 0, object)
		if nextObj != "N/A":
			clkObj(object, 0, nextObj)
		else:
			clkObj(object, 0, 1)
	else:
		sysMsg("Sufficient AP. Proceed to next step.")

def apCheckRDP(object, item=leaf120RDP, q=1, nextObj="N/A"):
	if exists(noAPRDP, normal):
		sysMsg("Insufficient AP.")
		clkObj(item)
		while q != 1:
			clkObj(leafAddRDP)
			q = q - 1
		clkObj(okAPRDP)
		clkObj(restoredAPRDP, 0, object)
		if nextObj != "N/A":
			clkObj(object, 0, nextObj)
		else:
			clkObj(object, 0, 1)
	else:
		sysMsg("Sufficient AP. Proceed to next step.")


# Rune check. If full, go to rune disassembly page.
def runeCheck():
	if exists(runeFull):
		sysMsg("Rune storage fulled. Going to rune disassembly page.")
		clkObj(runeFull, remark="OK button - rune full message")
		clkObj(back)
		sleep(changePage)
		clkObj(mainMenu)
		sleep(normal)
		clkObj(unit, 0, 1)
		sleep(changePage)
		clkObj(disassembly)
		exit()
	else:
		sysMsg("Rune check passed")

# After entering battle, toggle Auto if not On, and complete.
def btAction(loop=0, m=0):
	sysMsg("///// Executing btAction(loop=" + str(loop) + ") /////")
	while loop > -1:
		t = 0
		waitObj(btMenu, long)
		if exists(toggleAuto, normal):
			clkObj(toggleAuto)
			sysMsg("Toggled auto.")
			sleep(short)
		else:
			sysMsg("Auto already on.")
		while t != -1:
			if not exists(questMission, 0):
				sysMsg("Still in battle. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")
				if t > 1800:
					sysMsg("Timeout (30 min)")
					exit()
				else:
					t = t + 10
					sleep(10)
			else:
				sysMsg("Quest completed.")
				clkObj(questMission, loop=1)
				t = -1
		click()
		while exists(visionMax):
			sysMsg("Vision achieved.")
			sleep(5)
			clkObj(visionMax, remark="visionMax")
		if merchantCheck(m) == 1:
			m = 1
		if loop == 0:
			sysMsg("No more remaining loop. Returning to stage selection page.")
			sleep(changePage)
			clkObj(btEnd)
			mouseMove(10,0)
			click()
			loop = -1
		else:
			loop = loop - 1
			sysMsg("Restarting battle, remaining loop = " + str(loop) + ".")
			clkObj(btAgain)
			mouseMove(10,0)
			if merchantCheck(m) == 1:
				m = 1
			clkObj(btAgain)
			sleep(2)
			apCheck(btAgain)
			clkObj(btStart)
			sleep(1)
			if exists(noQuota, 0):
				sysMsg("No more quota for today. Terminating the loop and returning to stage selection page.")
				clkObj(noQuotaOK)
				clkObj(back)
				loop = -1
	sysMsg("///// End of btAction /////")

# After entering battle, quit.
def btQuit():
	clkObj(btMenu)
	clkObj(quitQuest)
	clkObj(confirm)


# Select team
# Tower: Page 1 [1-7] // Page 2 [8-12] // Page 3 [13-16] // Page 4 [17-20]
def teamSelect(position, page=1):
	p = 1
	sysMsg("Changing team @ page " + str(page))
	clkObj(teamArrow)
	sleep(normal)
	while p < page:
		clkObj(teamNext)
		p = p + 1
		sysMsg("Turned to team page " + str(page))
	clkObj(position)
	sysMsg("Team changed to " + str(position))

def merchantCheck(m=0):
	if m == 0:
		sysMsg("Checking if travelling merchant arrives.")
		if exists(peddlerShop, 5):
			sysMsg("Travelling merchant appears.")
			clkObj(peddlerShop)
		else:
			sysMsg("Travelling merchant not found.")
	else:
		sysMsg("Merchant check has been disabled.")
	return m

# Get reward from completed mission
def getReward():
	clkObj(mainMenu)
	clkObj(missionNew)
	while exists(rewardGet):
		clkObj(rewardGet, None, True)
		sleep(normal)
		type(Key.ESC)
	sysMsg("Claimed reward")

def enableAR():
	clkObj(arMenu)
	if exists(noAR, 2):
		sysMsg("Failed to initial auto repeat function.")
		clkObj(noQuotaOK)
		return 0
	else:
		clkObj(arMax)
		#clkObj(arRefillAP)
		clkObj(arStart)
		while not exists(okAR, 0):
			sleep(3)
			#if exists(arStart, 0):
				#clkObj(arStart)
		clkObj(okAR, 0, settings)
		return 1

# Check whether auto repeat has completed, and claim reward
def arCheck(loop=1):
	sysMsg("Checking status for auto repeat.")
	if not exists(autoRepeat, 0):
		sysMsg("Auto repeat has not activated.")
	else:
		arRegion = Region(find(autoRepeat).x, find(autoRepeat).y - 65, find(autoRepeat).w, find(autoRepeat).h + 65)
		while loop > 0:
			t = 0
			while not arRegion.exists(arComplete, 0):
			#while not exists(arComplete, 0):
				sysMsg("Auto repeat has not completed yet. Total waiting time: " + str(t/2) + " min.")					
				mouseMove(10,0)
				sleep(30)
				t = t + 1
			else:
				sysMsg("Auto repeat has completed. Total waiting time: " + str(t/2) + " min.")
			clkObj(autoRepeat, 0, arReward)
			clkObj(arReward, 0, arEnd)
			clkObj(arEnd)
			clkObj(confirm)
			sleep(2)
			clkObj(okAR)
			sleep(5)
			merchantCheck()
			if loop == "return":
				clkObj(arReturn)
				loop = 0
			elif loop > 1:
				sysMsg("Repeating the same stage. Remaining loop: " + str(loop))
				enableAR()
				loop = loop - 1
			else:
				sysMsg("Auto repeat completed")
				clkObj(arReturnHome)
				sleep(5)

sysMsg("Imported tagatame.sikuli")