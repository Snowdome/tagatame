# PoK.py last updated 16/10/2019
#  -------------------------Import Modules-------------------------
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
msgCount = "***************Successfully executed " + str(i) + " time(s)**************"
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

# Click icon (optional: delay = length(ms), loop = repeat until no longer exists, remark = use class.remark or customized message on log)
def clkIco(icon, delay=None, loop=False, remark=0):
	if remark == 0:
		obj = repr(icon)
	else:
		if remark == 1:
			obj = icon.remark
		else:
			obj = remark
	if not exists(icon):
		sysMsg("Waiting for " + obj)
		wait(icon, wTime)
	if delay != None:
		sysMsg("Delay clicking on " + obj + " for length = " + str(delay))
		sleep(delay)
	if loop == False:
		click(icon)
		sysMsg("Clicked on " + obj)
	else:
		try:
			click(icon)
			sysMsg("Clicked on " + obj + " for the 1st time")
			sleep(double)
			while exists(icon, changePage):
				click(icon)
				hover("start.png")
				sysMsg("Repeat clicking on " + obj)
				sleep(double)
			else:
				sysMsg("Finished looping on " + obj)
		except FindFailed:
			sysMsg("Cannot find icon")


# Enhance hime with chosen doll
def enhance(doll, n=1):
	sysMsg("Initializing Enhance command")
	i = 0
	while i < n:
		clkIco(himeEn)
		clkIco(doll)
		clkIco(OK)
		clkIco(confirm)
		clkIco(enStart)
		clkIco(yes)
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
		clkIco(gearForge)
		clkIco(selectOre)
		clkIco(confirm)
		clkIco(forgeStart)
		clkIco(yes)
		sleep(double)
		click(atMouse())
		sleep(double)
		click(atMouse())
		#while not exists(pageBack):
		#	click(atMouse())
		#	sleep(short)
		clkIco(pageBack)
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
		clkIco(dollMax)
		clkIco(skip)
		clkIco(pageNext)
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
		clkIco(ticket)
		if not exists(noMulti, short):
			clkIco(drawMax)
			clkIco(skip)
			clkIco(pageNext)
			sleep(double)
		else:
			clkIco(drawOnce)
			clkIco(skip)
			clkIco(pageBack)
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
		clkIco(btStart)
		wait(btResult, FOREVER)
		sleep(normal)
		while exists(affinity):
			click(affinity)
			sleep(double)
		clkIco(btResult, normal, True, remark = "btResult")
		clkIco(loot, normal, True)
		clkIco(btAgain)
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
		clkIco(btStart)
		wait(btResult, FOREVER)
		while exists(affinity):
			click(affinity)
			sleep(double)
		while exists(btResult):
			clkIco(btResult, loading, remark = "btResult")
		clkIco(loot, changePage)
		clkIco(pt, changePage)
		clkIco(accPt, double)
		while not exists(btAgain):
			clkIco(ptAch, double)
			sleep(double)
		clkIco(btAgain)
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
			clkIco(btAgain)
		clkIco(btStart)
		wait(btResult, FOREVER)
		clkIco(btResult, loading, remark = "btResult")
		while not exists(pageNext):
			click(atMouse())
			sleep(normal)
		clkIco(pageNext, changePage)
		while not exists(btAgain):
			click(atMouse())
			sleep(double)
		clkIco(btAgain)
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
	clkIco(menuBack)
	clkIco(train)
	clkIco(himeRe)
	clkIco(reConfirm)
	clkIco(yes)
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	clkIco(btStart)
	clkIco(btResult, changePage, remark = "btResult")
	sleep(double)
	click(atMouse())
	if exists(OK):
		clkIco(OK)
	clkIco(btResult, double, True, remark = "btResult")
	clkIco(loot, double, True)
	clkIco(btEndNext)
	clkIco(keyUnlock)
	clkIco(keyLv3)
	clkIco(yes)
	clkIco(keyStg, changePage)
	clkIco(unit1)
	clkIco(gear1)
	clkIco(egg)
	clkIco(confirm)
	clkIco(stats)
	

#  -------------------------Script-------------------------
#keyLv()
#btAction(3)
#btPtQuest(8)
btUnitQuest(50)
#forge(50)
#enhance(dollWhite, 23)
#drawTicket()