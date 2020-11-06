# PoK.py last updated 04/11/2020
#  -------------------------Import Modules and Class-------------------------
from sikuli import *

import time

#  -------------------------Global Setting-------------------------
Settings.MinSimilarity = 0.8

# Waiting time
short = 0.1
normal = 1
double = 2
changePage = 5
extend = 7
long = 180
battle = 300
wTime = 10

i = 0
msgError = "Error: n must be empty or positive"
msgEnd = "***************End of command***************"

#  -------------------------Assets-------------------------
# Draw
ticket = Pattern("ticket.png").targetOffset(0,125)
drawMax = Pattern("gachuHeader.png").targetOffset(135,275)	# Location of max button in respect to title bar
noTicket = "noTicket.png"
drawOK = "drawOK.png"
skip = "skip.png"
redraw = "redraw.png"
pageNext = "pageNext.png"
pageBack = "pageBack.png"

# Hime enchancement
himeEn = Pattern("himeEn.png").targetOffset(0,270)
dollWhite = "dollWhite.png"
dollBlack = "dollBlack.png"
dollBrown = "dollBrown.png"
dollPurple = "dollPurple.png"
OK = "OK.png"
confirm = "confirm.png"
enStart = "enStart.png"

# Gear forge
selectGear = Pattern("selectGear.png").targetOffset(-45,70)
gearForge = Pattern("gearForge.png").targetOffset(-10,315)
selectOre = Pattern("selectOre.png").targetOffset(-35,70)

forgeStart = "forgeStart.png"
yes = "yes.png"

# Battle
btMenu = "btMenu.png"
stageMission = "stageMission.png"
affinity = Pattern("affinity.png").similar(0.80)
btResult = Pattern("btResult.png").similar(0.90)
loot = "loot.png"
pt = Pattern("pt.png").targetOffset(110,575)
accPt = "accPt.png"
ptAch = "ptAch.png"
btAgain = "btAgain.png"
btEndNext = "btEndNext.png"
btAP = "btAP.png"
btStart = "btStart.png"
btMenu = "btMenu.png"
keyUnlock = Pattern("keyUnlock.png").similar(0.80)
keyLv3 = "keyLv3.png"
keyStg = Pattern("keyStg.png").targetOffset(130,415)

egg = Pattern("egg.png").similar(0.90)
stats = "stats.png" 
train = "train.png"
himeRe = "himeRe.png"
menuBack = "menuBack.png"
reConfirm = "reConfirm.png"

unit1 = Pattern("unit1.png").targetOffset(-215,-155)	#Offset for 1st unit slot
gear1 = Pattern("gear1.png").targetOffset(-30,60)	#Offset for 1st gear slot

# Tower event
challenge = "challenge.png"
setup = "setup.png"
btSummary = "btSummary.png"
towerReward = "towerReward.png"

#  -------------------------Define Function-------------------------
# Debug message
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

# Click object (optional: delay = length(sec), loop = repeat until no longer exists, remark = use class.remark or customized message on log)
def clkObj(object, delay=0, loop=0, remark=0):
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
		sysMsg("Cannot find " + subject + ". Please choose: [0]Retry, [1]Skip, [2]Terminate", "FindFailed Error (clkObj)", object)



# Enhance hime with chosen doll
def enhance(doll, n=1):
	sysMsg("Initializing Enhance command")
	i = 0
	while i < n:
		clkObj(himeEn)
		clkObj(doll)
		clkObj(OK)
		clkObj(confirm)
		clkObj(enStart)
		clkObj(yes)
		while not exists(himeEn):
			click(atMouse())
			sleep(short)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Forge first gear with first ore
def forge(n=1):
	sysMsg("Initializing Forge command")
	i = 0
	while i < n:
		clkObj(gearForge)
		clkObj(selectOre)
		clkObj(confirm)
		clkObj(forgeStart)
		clkObj(yes)
		sleep(double)
		click(atMouse())
		sleep(double)
		click(atMouse())
		#while not exists(pageBack):
		#	click(atMouse())
		#	sleep(short)
		clkObj(pageBack)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Draw dolls
def drawDoll(n=1):
	sysMsg("Initializing DrawDoll command")
	i = 0
	while i < n:
		clkObj(dollMax)
		clkObj(skip)
		clkObj(pageNext)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Draw ticket
def drawTicket(n=1):
	sysMsg("Initializing DrawTicket command")
	i = 0
	clkObj(ticket, 0, 0, "1st ticket")
	if n != "all":
		while i < n:
			clkObj(drawMax, 0, 0, "drawMax")
			clkObj(drawOK)
			clkObj(skip, 0, 1)
			i = i + 1
			sysMsg("*************** Successfully executed " + str(i) + " time(s) **************")
			if i < n:
				if exists(redraw):
					clkObj(redraw)
				else:
					if exists(pageNext, 0):
						clkObj(pageNext)
			else:		
				pass
	else:
		while i != -1:
			clkObj(drawMax, 0, 0, "drawMax")
			clkObj(drawOK)
			clkObj(skip, 1, 1)
			i = i + 1
			sysMsg("*************** Successfully executed " + str(i) + " time(s) **************")
			if exists(redraw):
				clkObj(redraw)
			else:
				if exists(pageNext, 0):
					clkObj(pageNext)
					sleep(changePage)
					clkObj(ticket, 0, 0, "1st ticket")
		else:
			if n < 0:
				sysMsg(msgError)
			else:
				sysMsg(msgEnd)

# Start battle for normal quest
def btAction(n=1):
	sysMsg("Initializing BattleAction command")
	i = 0
	while i < n:
		clkObj(btStart)
		wait(btResult, FOREVER)
		sleep(normal)
		while exists(affinity):
			click(affinity)
			sleep(double)
		clkObj(btResult, normal, True, remark = "btResult")
		clkObj(loot, normal, True)
		clkObj(btAgain)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Start battle for unit quest
def btPtQuest(n=1):
	sysMsg("Initializing UnitQuest command")
	i = 0
	while i < n:
		try:
			if exists(btAgain, normal):
				clkObj(btAgain)
			clkObj(btStart)
			t = 0
			while t != -1:
				if exists(btMenu, 0):
					t = t + 10
					sleep (10)
					sysMsg("Battle in progress. Waiting for 10 more sec. Total waiting time: " + str(t) + "sec.")
				else:
					if exists(btResult, 0):
						sysMsg("***************btResult found***************")
						t = -1
						clkObj(btResult, double, 0, remark = "btResult")
			while not exists(pageNext):
				click(atMouse())
				sleep(normal)
			clkObj(pageNext, changePage)
			while not exists(btAgain):
				click(atMouse())
				sleep(double)
			clkObj(btAgain)
			i = i + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
			sleep(normal)
		except FindFailed:
			sysMsg("FindFailed! Need further examination.")
	else:
		if n <= 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)


# Start battle for unit quest
def btUnitQuest(n=1):
	sysMsg("Initializing UnitQuest command")
	i = 0
	while i < n:
		try:
			if exists(btAgain, normal):
				clkObj(btAgain)
			clkObj(btStart)
			wait(btResult, FOREVER)
			clkObj(btResult, double, 0, remark = "btResult")
			while not exists(pageNext):
				click(atMouse())
				sleep(normal)
			clkObj(pageNext, changePage)
			while not exists(btAgain):
				click(atMouse())
				sleep(double)
			clkObj(btAgain)
			i = i + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
			sleep(normal)
		except FindFailed:
			sysMsg("FindFailed! Need further examination.")
	else:
		if n <= 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Start battle for normal quest
def btQuest(n=1):
	sysMsg("Initializing BtQuest command")
	i = 0
	while i < n:
		try:
			if exists(btAgain, normal):
				clkObj(btAgain)
			clkObj(btStart)
			wait(btResult, FOREVER)
			clkObj(btResult, double, 0, remark = "btResult")
			while not exists(btAgain):
				click(atMouse())
				sleep(double)
			clkObj(btAgain)
			i = i + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
			sleep(normal)
		except FindFailed:
			sysMsg("FindFailed! Need further examination.")
	else:
		if n <= 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)


# Starting from stats menu, reincarnate and level up via key stage
def keyLv():
	clkObj(menuBack)
	clkObj(train)
	clkObj(himeRe)
	clkObj(reConfirm)
	clkObj(yes)
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	clkObj(btStart)
	clkObj(btResult, changePage, remark = "btResult")
	sleep(double)
	click(atMouse())
	if exists(OK):
		clkObj(OK)
	clkObj(btResult, double, True, remark = "btResult")
	clkObj(loot, double, True)
	clkObj(btEndNext)
	clkObj(keyUnlock)
	clkObj(keyLv3)
	clkObj(yes)
	clkObj(keyStg, changePage)
	clkObj(unit1)
	clkObj(gear1)
	clkObj(egg)
	clkObj(confirm)
	clkObj(stats)
	

# Auto Tower
def autoTower():
	i = 0
	e = 1
	while i != -1:
		if not exists(btStart, 0):
			clkObj(challenge)
			if exists(setup):
				e = 0
			while e == 0:
				sysMsg("Cannot find Start button. \nPress Yes after team has been fixed and returned to preparation screen.", "Team Composition Error")
				if exists(btStart, 0):
					e = 1
		t = 0
		clkObj(btStart)
		while t != -1:
			if exists(challenge, 0):
				sysMsg("Returned to Battle Preparation")
				t = -1
			else:
				if exists(btSummary):
					i = i + 1
					sysMsg("*************** " + str(i) + " floor(s) cleared ***************")
					clkObj(btSummary)
					clkObj(towerReward)
					sleep(normal)
					click(atMouse())
					t = -1
				else:
					t = t + 10	
					sleep(10)
					sysMsg("Completion message not found. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")
	sysMsg("End of command")

#  -------------------------Script-------------------------
#keyLv()
#btAction(3)
#btPtQuest(20)
#btUnitQuest(999)
#btQuest(4)
#forge(50-7)
#enhance(dollWhite, 23)
#drawTicket("all")
#drawDoll(100)
autoTower()