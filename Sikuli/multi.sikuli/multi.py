# multi.py last updated 12/02/2020

#  -------------------------Import Modules and Classes-------------------------
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
subArrow = Pattern("1581461703200.png").targetOffset(-130,390)	# Location of down arrow in respect to the menu in sub-window
subCreateRoom = "subCreateRoom.png"
subPrivate = Pattern("subPrivate.png").similar(0.90).targetOffset(100,0)
subConfirmCreate = "subConfirmCreate.png"
subInvite = "subInvite.png"
subIniteSlot1 = Pattern("subIniteSlot1.png").targetOffset(-100,60)	# Location of down arrow in respect to the message in sub-window
subAdded = Pattern("subAdded.png").similar(0.80)
subConfirmInvite = Pattern("subConfirmInvite.png").similar(0.90)
mainInvite = "mainInvite.png"
inviteError = Pattern("inviteError.png").targetOffset(245,-255)
mainInviteSlot1 = Pattern("mainInviteSlot1.png").targetOffset(375,100)	# Location of down arrow in respect to the header in main-window
ready = "ready.png"
subBtStart = "subBtStart.png"
subBtMenu = "subBtMenu.png"
subRetreatBtn = Pattern("subRetreatBtn.png").similar(0.80)
subConfirm = "subConfirm.png"
OK = Pattern("OK.png").similar(0.80)
loadingScreen = "loadingScreen.png"
# Finished
# rdpOK
# rdpHome
# rdpMsg

mRec = "mRec.png"
mRecBtn = "mRecBtn.png"
s105 = Pattern("s105.png").targetOffset(150,0)
sS2b = Pattern("sS2b.png").targetOffset(150,0)
s102 = Pattern("s102.png").targetOffset(150,0)
	

# -------------------------Multi Action-------------------------
# Main interface
title = "screen"

# Battle interface
end = "end.png"
atk = Pattern("end.png").targetOffset(-190,-15)	# Locaation of Attack button in respec to End button
mainSkill = Pattern("end.png").targetOffset(-100,-50)	# Locaation of Main Skill button in respec to End button
subSkill = Pattern("end.png").targetOffset(-30,-125)	# Locaation of Sub Skill button in respec to End button
masterSkill = Pattern("end.png").targetOffset(10,-220)	# Locaation of Master Art button in respec to End button
cancel = "cancel.png"
actOK = "actOK.png"
skillDown = "skillDown.png"
skill1 = Pattern("skillDown.png").targetOffset(-190,120)
skill2 = Pattern("skillDown.png").targetOffset(-190,260)
skill3 = Pattern("skillDown.png").targetOffset(-190,420)


#  -------------------------Saved automation-------------------------
def subRetreat():
	clkObj(subBtMenu)
	clkObj(subRetreatBtn)
	clkObj(subConfirm)
	clkObj(OK)

def actm202():
	sysMsg("Executing Main-Act 202")
	sysMsg("レティシア uses 2nd main skill - 銀彩ルサールカ, stays and end turn")
	clkObj(mainSkill)
	clkObj(skill2)
	clkObj(actOK)
	subRetreat()
	clkObj(end)
	clkObj(actOK)	
	sysMsg("Step 2: クリーマ uses 5th main skill - 長雨カタツムリ, stays and end turn")
	clkObj(mainSkill)
	clkObj(skillDown)
	clkObj(skillDown)
	clkObj(skill3)
	clkObj(actOK)
	clkObj(end)
	clkObj(actOK)
	sysMsg("レティシア stays and end turn")
	clkObj(end)
	clkObj(actOK)
	sysMsg("Step 4: クリーマ uses 5th main skill - 長雨カタツムリ, stays and end turn")
	clkObj(mainSkill)
	clkObj(skillDown)
	clkObj(skillDown)
	clkObj(skill3)
	clkObj(actOK)
	clkObj(end)
	clkObj(actOK)
	sysMsg("Step 5: レティシア stays and end turn")
	clkObj(end)
	clkObj(actOK)
	sysMsg("Step 6: クリーマ uses 5th main skill - 長雨カタツムリ, quest completed")
	clkObj(mainSkill)
	clkObj(skillDown)
	clkObj(skillDown)
	clkObj(skill3)
	clkObj(actOK)

def acts105():
	sysMsg("Executing Sub-Act 105")
	clkObj(atk, remark="Attack")
	clkObj(cancel)
	subRetreat()
	clkObj(s105)

def actS2b():
	sysMsg("Executing Sub-Act Sin2B")
	clkObj(atk, remark="Attack")
	clkObj(cancel)
	subRetreat()
	clkObj(sS2b)

def acts102():
	sysMsg("Executing Sub-Act 102")
	clkObj(atk, remark="Attack")
	clkObj(cancel)
	subRetreat()
	clkObj(s102)

#  -------------------------Variables-------------------------
gain = "gain.png"
zin = "zin.png"


sin = "sin.png"
sin2a = Pattern("stg1.png").exact()
mainCh1 = "mainCh1.png"
mainStg105 = Pattern("mainStg05.png").similar(0.95)
solo105 = multiQ(mainCh1, mainStg105)

# Ch1: double team seiseki
# Ch2: normal seiseki
subCh1 = "subCh1.png"	# 2-player quest
subStg102 = "subStg102.png"
subStg105 = "subStg105.png"
subCh2 = "subCh2.png"	# 4-player quest
subStg205 = "subStg205.png"
sub102 = multiQ(subCh1, subStg102)
sub105 = multiQ(subCh1, subStg105)
sub205 = multiQ(subCh2, subStg205)
subSin = "subSin.png"
subSin2b = Pattern("subSin2b.png").similar(0.95)
subS2b = multiQ(subSin, subSin2b)

#  -------------------------Define Function-------------------------
# Choose unit
def myUnit(object):
	click(myUnit)
	while not exists(object):
		click(arrowRight)
		sysMsg("Turning page: character")
	click(object)


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
			clkObj(multi)
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
		clkObj(multiQ.stage)
		click(createRoom)
		if exists(private, double):
			clkObj(private)
		else:
			sysMsg("Room is already private")
		click(confirmCreate)


def gotoSubMulti(multiQ):
	if not exists(subInvite, short):
		sysMsg("[Sub] Going to selected multi quest")
		if not exists(subMyUnit, short):
			if not exists(subMultiMenu, short):		
				if exists(subHome, short):
					clkObj(subHome)
				clkObj(subQuest)
				clkObj(subMulti)
				wait(subMultiMenu, FOREVER)
			while not exists(multiQ.chapter, double):
				clkObj(subArrow, remark="[Sub]Arrow")
				sysMsg("[Sub] Turning page: chapter")
			clkObj(multiQ.chapter)
			sleep(double)
		while not exists(multiQ.stage, double):
			clkObj(subArrow, remark="[Sub]Arrow")
			sysMsg("[Sub] Turning page: stage")
		clkObj(multiQ.stage)
		clkObj(subCreateRoom)
		if exists(subPrivate, double):
			clkObj(subPrivate)
		else:
			sysMsg("Room is already private")
		clkObj(subConfirmCreate)
	else:
		sysMsg("[Sub] Aleady in multi quest preparation page")
		

def multiSingle(multiQ, script, n=0):
	sysMsg("Initializing MultiSingle command")
	i = 0
	if not exists(mRec, 0):
		sysMsg("Cannot find Macro Recorder.\nPress Yes after the window has been opened.", "Setup error")
	if not exists(btStart, short):
		gotoMulti(multiQ)
	while i < n:
		clkObj(multiStart)
		apCheck(multiStart)
		clkObj(confirm)
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
	if not exists(mRec, 0):
		sysMsg("Cannot find Macro Recorder.\nPress Yes after the window has been opened.", "Setup error")
	gotoSubMulti(multiQ)
	# Sub send invitation (slot 1)
	clkObj(subInvite)
	clkObj(subIniteSlot1)
	if exists(subAdded):
		clkObj(subConfirmInvite, 0, True)
	else:
		while not exists(subAdded):
			clkObj(subIniteSlot1)
			clkObj(subConfirmInvite, 0, True)
	while i < n:
		# Main accept invitation
		if exists(home):
			clkObj(home)
		clkObj(mainInvite)
		while exists(inviteError, double):
			clkObj(inviteError)
			if exists(subInvite, normal):
				clkObj(subInvite)
			if exists(subInviteSlot1):
				clkObj(subIniteSlot1)
				clkObj(subAdded)
			if exists(subConfirmInvite):
				clkObj(subConfirmInvite, 0, True)
			clkObj(mainInvite)
		else:
			clkObj(mainInviteSlot1)
			clkObj(ready)
			sleep(double)
		# Sub start multi quest and retreat
		clkObj(subBtStart)
		if exists(subConfirm, short):
			clkObj(subConfirm)
		sleep(normal)
		if not exists(loadingScreen, 15):
			sysMsg("Cannot find loaning screen. Retrying.")
			mouseMove(10,0)
			clkObj(subBtStart)
			if exists(subConfirm, 0):
				clkObj(subConfirm)
		sysMsg("Entering battle")
		wait(end, FOREVER)
		### Nox disconnect script here ###
#		if exists(title):
#			clkObj(title)
#			clkObj(OK)
#			sysMsg("Nox has reconnected")
		# Executed saved action
		script()
		# multiAction(multiQ.action)
		#	   if exists(questFailed, 180):
		#		   clkObj(questFailed)
		#		   sysMsg("Quest failed")
		# Remote Desktop completed quest
		#if exists(finished):
		#	sysMsg("Quest completed")
		if i + 1 < n:
			wait(subHome, 30)
			gotoSubMulti(multiQ)
			# Sub send invitation (slot 1)
			clkObj(subInvite)
			clkObj(subIniteSlot1)
			if exists(subAdded):
				clkObj(subConfirmInvite, 0, True)
			else:
				while not exists(subAdded):
					clkObj(subIniteSlot1)
					clkObj(subConfirmInvite, 0, True)
		wait(finished, FOREVER)
		sleep(extend)
		clkObj(finished)
		mouseMove(10,0)
		click(atMouse())
		wait(OK, 30)
		clkObj(OK)
		clkObj(home, double)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		pass



#  -------------------------Body-------------------------
#multiSingle(solo105, actm105, 1000)
#multiDouble(sub205, acts105, 1000)
#multiDouble(subS2b, actsS2b, 1000)
multiDouble(sub102, acts102, 1000)