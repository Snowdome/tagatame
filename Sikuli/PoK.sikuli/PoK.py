# PoK.py last updated 27/10/2019
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
loading = 12
long = 180
wTime = FOREVER

i = 0
msgError = "Error: n must be empty or positive"
msgEnd = "***************End of function***************"

#  -------------------------Assets-------------------------
# Draw
ticket = Pattern("ticket.png").targetOffset(0,125)
drawOnce = Pattern("gachuHeader.png").targetOffset(-95,230)
drawMax = Pattern("gachuHeader.png").targetOffset(85,230)
noMulti = Pattern("noMulti.png").exact()
dollMax = "dollMax.png"
noTicket = "noTicket.png"
skip = "skip.png"
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


#  -------------------------Define Function-------------------------
# Debug message
def sysMsg(text):
	now = time.localtime()
	print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + text)

# Click object (optional: delay = length(sec), loop = repeat until no longer exists, remark = use class.remark or customized message on log)
def clkObj(object, delay=0, loop=0, remark=0):
	if remark == 0:
		subject = repr(object)
	else:
		if remark == 1:	# Not yet implemented
			subject = object.remark
		else:
			subject = remark
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
		while exists(object):
			try:
				click(object)
				sleep(normal)
				mouseMove(10,0)
				sysMsg("Repeat clicking on " + subject)
			except FindFailed:
				sysMsg("Cannot find object")



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
	while i < n:
		clkObj(ticket)
		if not exists(noMulti, short):
			clkObj(drawMax)
			clkObj(skip)
			clkObj(pageNext)
			sleep(double)
		else:
			clkObj(drawOnce)
			clkObj(skip)
			clkObj(pageBack)
			sleep(double)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
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

# Start battle for point quest
def btPtQuest(n=1):
	sysMsg("Initializing BattlePointQuest command")
	i = 0
	while i < n:
		clkObj(btStart)
		wait(btResult, FOREVER)
		while exists(affinity):
			click(affinity)
			sleep(double)
		while exists(btResult):
			clkObj(btResult, loading, remark = "btResult")
		clkObj(loot, changePage)
		clkObj(pt, changePage)
		clkObj(accPt, double)
		while not exists(btAgain):
			clkObj(ptAch, double)
			sleep(double)
		clkObj(btAgain)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
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
		if exists(btAgain, normal):
			clkObj(btAgain)
		clkObj(btStart)
		wait(btResult, FOREVER)
		clkObj(btResult, loading, remark = "btResult")
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
	

#  -------------------------Script-------------------------
#keyLv()
#btAction(3)
#btPtQuest(8)
#btUnitQuest(50)
#forge(50)
#enhance(dollWhite, 23)
#drawTicket()
drawDoll(100)