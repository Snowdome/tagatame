# multi.py last updated 18/09/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

# Define class for multi quest
class multiQ(object):
	def __init__(self, chapter, stage, title):
		self.chapter = chapter
		self.stage = stage
		self.title = title

#  -------------------------Assets-------------------------
multi = "multi.png"
teamEdit = "teamEdit.png"
myUnit = "teamEdit.png"
multiList = "multiList.png"
arrowRight = Pattern("arrowRight.png").targetOffset(20,198)	# Location of right arrow in respect to the close button
createRoom = "createRoom.png"
private = Pattern("private.png").similar(0.90).targetOffset(110,0)
confirmCreate = "confirmCreate.png"
multiStart = "multiStart.png"
questFailed = Pattern("questFailed.png").targetOffset(20,143)
dc = Pattern("dc.png").targetOffset(0,240)	# Location of OK button in respect to the message
finished = "finished.png"

subHome = "subHome.png"
subQuest = Pattern("1581461703200.png").targetOffset(-65,360)	# Location of quest button in respect to the menu in sub-window
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
s102 = Pattern("s102.png").similar(0.80).targetOffset(147,0)
nero = Pattern("nero.png").targetOffset(150,0)
	

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

def neroSolo():
	sysMsg("Executing neroSolo macro.")
	clkObj(nero)

#  -------------------------Variables-------------------------
gain = "gain.png"
zin = "zin.png"


sin = "sin.png"
sin2a = Pattern("stg1.png").exact()
mainCh1 = "mainCh1.png"
solo105 = multiQ(mainCh1, "main105Stage.png", "main105Title.png")

soloXmas = multiQ("mainXmasCh.png", "mainXmasStage.png", "mainXmasTitle.png")
soloZahar = multiQ(Pattern("zaharCh.png").targetOffset(100,0), "zaharStage.png", "zaharTitle.png")
soloZaharI = multiQ(Pattern("zaharCh.png").targetOffset(100,0), "1600393931083.png", "1600393951157.png")

# Ch1: double team seiseki
# Ch2: normal seiseki
subCh1 = "subCh1.png"	# 2-player quest
sub102 = multiQ(subCh1, "subStg102.png", "dummy")
sub105 = multiQ(subCh1, "subStg105.png", "dummy")

subCh2 = "subCh2.png"	# 4-player quest
sub205 = multiQ(subCh2, "subStg205.png", "dummy")

subSin = "subSin.png"
subS2b = multiQ(subSin, Pattern("subSin2b.png").similar(0.95), "dummy")

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
	if exists(multiQ.title, 0):
		sysMsg("Already in selected multi quest preparation menu.")
	else:
		if not exists(multiQ.stage):
			if not exists(multiList, 0):
				if not exists(settings, 0):
					clkObj(home, 0, quest)
				clkObj(quest, 0, multi)
				clkObj(multi, 0, multiList)
			else:
				sysMsg("Already in Multi Quest selection menu")
			sleep(8)
			while not exists(multiQ.chapter, double):
				clkObj(questArrow, remark="Quest Arrow")
				sysMsg("Turning page: chapter")
			while exists(multiList, 0):
				clkObj(multiQ.chapter)
				mouseMove(10,0)
				sleep(2)
			while not exists(multiQ.stage, double):
				clkObj(questArrow, remark="Quest Arrow")
				sysMsg("Turning page: stage")
		clkObj(multiQ.stage)
		clkObj(createRoom)
		if exists(private, double):
			clkObj(private)
		else:
			sysMsg("Room is already private")
		clkObj(confirmCreate)


def gotoSubMulti(multiQ):
	if not exists(subInvite, short):
		sysMsg("[Sub] Going to selected multi quest")
		if not exists(subMyUnit, short):
			if not exists(subMultiMenu, short):		
				if exists(subHome, short):
					clkObj(subHome)
				clkObj(subQuest, 0, subMulti, "suQuest Loc")
				clkObj(subMulti)
				waitObj(subMultiMenu, 300)
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
	waitObj(mRec, 0)
	if not exists(btStart, short):
		gotoMulti(multiQ)
	while i < n:
		sleep(3)
		clkObj(multiStart)
		apCheck(multiStart, nextObj=confirm)
		clkObj(confirm)
		sysMsg("Quest started")
		waitObj(btMenu, 30)
		if script != "auto":
			script()
		waitObj(finished, 360)
		clkObj(finished, 0, multiStart)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()


def multiDouble(multiQ, script, n=1):
	sysMsg("Initializing MultiDouble command")
	i = 0
	t = 0
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
			clkObj(mainInviteSlot1, 0, 0, "mainInviteSlot1 Loc")
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
		waitObj(end, 300)
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
			waitObj(subHome, 30)
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
		while t != -1:
			if exists(finished, 0):
				sysMsg("Main-window finish button found.")
				t = -1
			else:
				sleep(10)
				t = t + 10
				sysMsg("Main-window finish button not found. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")
		sleep(extend)
		if exists(OK, 0):
			sysMsg("Main-window timeout (Mode 2).")
			clkObj(OK)
			sleep(normal)
			clkObj(finished)
			mouseMove(10,0)
			click(atMouse())
		else:
			sysMsg("Main-window timeout. (Mode 1)")
			clkObj(finished)
			mouseMove(10,0)
			click(atMouse())
			sleep(5)
			clkObj(OK)
			sleep(normal)
		t = 0
		while t != -1:
			if exists(home):
				clkObj(home, double)
				t = -1
			else:
				sleep(5)
				t = t + 5
				sysMsg("Home button not found. Waiting for 5 more sec. Total waiting time: " + str(t) + " sec.")
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


#multiDouble(sub102, acts102, 500)
multiSingle(soloZaharI, "auto", 7)