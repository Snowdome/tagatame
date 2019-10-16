# multi.py last updated 15/10/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *

# Define class for multi quest
class multiQ(object):
	def __init__(self, chapter, stage):
		self.chapter = chapter
		self.stage = stage

#  -------------------------Assets-------------------------
multi = "multi.png"
teamEdit = "teamEdit.png"
myUnit = "teamEdit.png"
multiList = "multiList.png"
arrowRight = Pattern("arrowRight.png").targetOffset(20,198)	# Location of right arrow in respect to the close button
createRoom = "createRoom.png"
private = Pattern("private.png").similar(0.90).targetOffset(100,0)
confirmCreate = "confirmCreate.png"
multiStart = "multiStart.png"
questFailed = Pattern("questFailed.png").targetOffset(20,143)
dc = Pattern("dc.png").targetOffset(0,240)	# Location of OK button in respect to the message
finished = "finished.png"

subHome = "subHome.png"
subQuest = "subQuest.png"
subMulti = "subMulti.png"
subMultiMenu = "subMultiMenu.png"
subMyUnit = "subMyUnit.png"
subArrow = Pattern("subMenu.png").targetOffset(-130,380)	# Location of down arrow in respect to the menu in sub-window
subCreateRoom = "subCreateRoom.png"
subPrivate = Pattern("subPrivate.png").similar(0.90).targetOffset(100,0)
subConfirmCreate = "subConfirmCreate.png"
subInvite = "subInvite.png"
subIniteSlot1 = Pattern("subIniteSlot1.png").targetOffset(-100,60)	# Location of down arrow in respect to the message in sub-window
subAdded = Pattern("subAdded.png").similar(0.80)
subConfirmInvite = Pattern("subConfirmInvite.png").similar(0.80)
mainInvite = "mainInvite.png"
inviteError = "inviteError.png"
mainInviteSlot1 = Pattern("mainInviteSlot1.png").targetOffset(375,100)	# Location of down arrow in respect to the header in main-window
ready = "ready.png"
subBtStart = "subBtStart.png"
subBtMenu = "subBtMenu.png"
subRetreatBtn = "subRetreatBtn.png"
subConfirm = "subConfirm.png"
OK = Pattern("OK.png").similar(0.80)
# Finished
# rdpOK
# rdpHome
# rdpMsg

mRec = "mRec.png"
mRecBtn = "mRecBtn.png"
m105 = Pattern("m105.png").targetOffset(155,0)
	

# -------------------------Multi Action-------------------------
# Main interface
title = "screen"

# Battle interface
end = "end.png"
atk = Pattern("end.png").targetOffset(-190,-15)	# Locaation of Attack button in respec to End button
mainSkill = Pattern("end.png").targetOffset(-100,-50)	# Locaation of Main Skill button in respec to End button
subSkill = Pattern("end.png").targetOffset(-30,-125)	# Locaation of Sub Skill button in respec to End button
masterSkill = Pattern("end.png").targetOffset(10,-220)	# Locaation of Master Art button in respec to End button
actOK = "actOK.png"
skillDown = "skillDown.png"
skill1 = Pattern("skillDown.png").targetOffset(-190,120)
skill2 = Pattern("skillDown.png").targetOffset(-190,260)
skill3 = Pattern("skillDown.png").targetOffset(-190,420)


#  -------------------------Saved automation-------------------------
def noxMacro(icon):
	if not exists(mRec, 0):
		sysMsg("Opening Macro Recorder window")
		clkIco(mRecBtn)
		dragDrop(mRec, Pattern(mRec).targetOffset(760,0))
		sleep(normal)
	clkIco(icon)


def subRetreat():
	clkIco(subBtMenu)
	clkIco(subRetreatBtn)
	clkIco(subConfirm)
	clkIco(OK)


def act105():
	sysMsg("Executing Act 105")
	noxMacro(m105)
	if not exists(finished, 30):
		sysMsg("Cannot complete quest - target still alive? Attampting to restart the current quest.")
		btQuit()
		wait(quest, FOREVER)
		gotoMulti(solo105)
		clkIco(multiStart)
		wait(double)
		if exists(noAP, 1):
			resAP()
			clkIco(multiStart)
		clkIco(confirm)
		sysMsg("Quest restarted")
		wait(btMenu, FOREVER)
		noxMacro(m105)
		if not exists(finished, 30):
			sysMsg("Cannot complete quest twice - exiting")
			exit()
		else:
			clkIco(finished)
			sleep(changePage)
			esc(finished)
	else:
		sysMsg("Quest completed")
				

def act202():
	sysMsg("Executing Act 202")
	sysMsg("レティシア uses 2nd main skill - 銀彩ルサールカ, stays and end turn")
	clkIco(mainSkill)
	clkIco(skill2)
	clkIco(actOK)
	subRetreat()
	clkIco(end)
	clkIco(actOK)	
	sysMsg("Step 2: クリーマ uses 5th main skill - 長雨カタツムリ, stays and end turn")
	clkIco(mainSkill)
	clkIco(skillDown)
	clkIco(skillDown)
	clkIco(skill3)
	clkIco(actOK)
	clkIco(end)
	clkIco(actOK)
	sysMsg("レティシア stays and end turn")
	clkIco(end)
	clkIco(actOK)
	sysMsg("Step 4: クリーマ uses 5th main skill - 長雨カタツムリ, stays and end turn")
	clkIco(mainSkill)
	clkIco(skillDown)
	clkIco(skillDown)
	clkIco(skill3)
	clkIco(actOK)
	clkIco(end)
	clkIco(actOK)
	sysMsg("Step 5: レティシア stays and end turn")
	clkIco(end)
	clkIco(actOK)
	sysMsg("Step 6: クリーマ uses 5th main skill - 長雨カタツムリ, quest completed")
	clkIco(mainSkill)
	clkIco(skillDown)
	clkIco(skillDown)
	clkIco(skill3)
	clkIco(actOK)

def act205():
	subRetreat()
	noxMacro(m105)

#  -------------------------Variables-------------------------
gain = "gain.png"
zin = "zin.png"


sin = "sin.png"
sin2a = Pattern("stg1.png").exact()
mainCh1 = "mainCh1.png"
mainStg05 = Pattern("mainStg05.png").similar(0.95)
solo105 = multiQ(mainCh1, mainStg05)

# Ch1: double team seiseki
# Ch2: normal seiseki
subCh1 = "subCh1.png"
subStg102 = "subStg102.png"
subStg105 = "subStg105.png"
subCh2 = "subCh2.png"
subStg205 = "subStg205.png"
sub102 = multiQ(subCh1, subStg102)
sub105 = multiQ(subCh1, subStg105)
sub205 = multiQ(subCh2, subStg205)

#  -------------------------Define Function-------------------------
# Choose unit
def myUnit(icon):
	click(myUnit)
	while not exists(icon):
		click(arrowRight)
		sysMsg("Turning page: character")
	click(icon)


# Go to multi quest
def gotoMulti(multiQ):
	sysMsg("Going to selected multiplayer quest")
	if exists(multiStart):
		sysMsg("Battle Start button found. Double check location.")
	else:			
		if not exists(multiList, short):
			if not exists(settings, short):
				click(home)
				wait(quest, 20)
				sleep(double)
			click(quest)
			clkIco(multi)
			wait(multiList, FOREVER)
		else:
			sysMsg("Already in Multi Quest selection menu")
		while not exists(multiQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(multiQ.chapter)
		while not exists(multiQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		clkIco(multiQ.stage)
		click(createRoom)
		if exists(private, double):
			clkIco(private)
		else:
			sysMsg("Room is already private")
		click(confirmCreate)


def gotoSubMulti(multiQ):
	if not exists(subInvite, short):
		sysMsg("[Sub] Going to selected multi quest")
		if not exists(subMyUnit, short):
			if not exists(subMultiMenu, short):		
				if exists(subHome, short):
					clkIco(subHome)
				clkIco(subQuest)
				clkIco(subMulti)
				wait(subMultiMenu, FOREVER)
			while not exists(multiQ.chapter, double):
				clkIco(subArrow)
				sysMsg("[Sub] Turning page: chapter")
			clkIco(multiQ.chapter)
			sleep(double)
		while not exists(multiQ.stage, double):
			clkIco(subArrow)
			sysMsg("[Sub] Turning page: stage")
		clkIco(multiQ.stage)
		clkIco(subCreateRoom)
		if exists(subPrivate, double):
			clkIco(subPrivate)
		else:
			sysMsg("Room is already private")
		clkIco(subConfirmCreate)
	else:
		sysMsg("[Sub] Aleady in multi quest preparation page")
		

def multiSingle(multiQ, script, n=0):
	sysMsg("Initializing MultiSingle command")
	i = 0
	if not exists(btStart, short):
		gotoMulti(multiQ)
	while i < n:
		clkIco(multiStart)
		wait(normal)
		if exists(noAP, short):
			resAP()
			clkIco(multiStart)
		clkIco(confirm)
		sysMsg("Quest started")
		wait(btMenu, 30)
		script()
		sleep(changePage)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()


def multiDouble(multiQ, script, n=1):
	sysMsg("Initializing MultiDouble command")
	i = 0
	while i < n:
		gotoSubMulti(multiQ)
		# Sub send invitation (slot 1)
		clkIco(subInvite)
		clkIco(subIniteSlot1)
		clkIco(subAdded)
		clkIco(subConfirmInvite, None, True)
		# Main accept invitation
		if exists(home):
			clkIco(home)
		try:
			clkIco(mainInvite)
		except FindFailed:
			sysMsg("Error - no invitation message")
		clkIco(mainInviteSlot1)
		clkIco(ready)
		# Sub start multi quest and retreat
		try:
			clkIco(subBtStart, double, True)
			if exists(subConfirm):
				clkIco(subConfirm)
		except FindFailed:
			pass
		sysMsg("Entering battle")
		### Nox disconnect script here ###
#		if exists(title):
#			clkIco(title)
#			clkIco(OK)
#			sysMsg("Nox has reconnected")
		# Executed saved action
		script()
		# multiAction(multiQ.action)
		#	   if exists(questFailed, 180):
		#		   clkIco(questFailed)
		#		   sysMsg("Quest failed")
		# Remote Desktop completed quest
		#if exists(finished):
		#	sysMsg("Quest completed")
		sleep(extend)
		clkIco(finished)
		clkIco(OK)
		clkIco(home)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		pass



#  -------------------------Body-------------------------
#multiSingle(solo105, act105, 1000)
multiDouble(sub205, act205, 1000)