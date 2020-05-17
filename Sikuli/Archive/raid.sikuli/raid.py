# raid.py last updated 04/11/2019

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for raid boss and team
class raidQ():
	def __init__(self, boss, team):
		self.boss = boss
		self.team = team
		# self.mode = "mode"		# 1. guild only / 2. friend only / 3. guild or friend / 4. anyone
		# self.timeout = "timeout"	# how long until the withdraw from the assisted boss


#  -------------------------Settings-------------------------
resRP = 0	# Number of times allowed to restore RP before terminating the command.
raQuit = 10	# Time wait before quitting assisted boss. If set to 0, auto quit.
pokLoad = 0	# If 1, also auto PoK quest

#  -------------------------Assets-------------------------
assist = "assist.png"
aSlot1 = Pattern("assistList.png").targetOffset(165,100)	# Location in respect to the title bar
aSlot2 = Pattern("assistList.png").targetOffset(165,210)	# Location in respect to the title bar
aSlot3 = Pattern("assistList.png").targetOffset(165,315)	# Location in respect to the title bar
okAssist = Pattern("okAssist.png").targetOffset(95,410)	# Location in respect to the title bar
guild = "guild.png"
friend = "friend.png"
refresh = "refresh.png"
closeX = "closeX.png"
errDead = Pattern("errDead.png").targetOffset(0,240)	# Location in respect to the message
raidStart = "raidStart.png"
atkDmg = "atkDmg.png"
endMsg = "endMsg.png"
raidReward = "raidReward.png"
cfnReward = "cfnReward.png"
areaReward = "areaReward.png"
nextArea = Pattern("nextArea.png").targetOffset(100,225)
reset = "reset.png"
raidQuit = "raidQuit.png"
raidQuited = Pattern("raidQuited.png").targetOffset(0,235)	# Location of OK button in respect to the message
requestAid = "requestAid.png"
requestedAid = "requestedAid.png"
sendRequest = "sendRequest.png"
sentRequest = Pattern("sentRequest.png").targetOffset(-5,240)	# Location of OK button in respect to the message
raidBack1 = "raidBack1.png"
raidBack2 =	 "raidBack2.png"
fullRaid = Pattern("fullRaid.png").targetOffset(0,255)
killed = Pattern("killed.png").similar(0.90).targetOffset(-107,240)	# Location of OK button in respect to the message
addFd = Pattern("addFd.png").targetOffset(0,405)	# Location of yes button in respect to the title bar
noRP = Pattern("noRP.png").targetOffset(95,140)
restoredRP = Pattern("restoredRP.png").targetOffset(3,185)



#  -------------------------Variables-------------------------
team1 = team(slot1, 1)
team2 = team(slot2, 1)
team3 = team(slot3, 1)
team4 = team(slot4, 1)
team5 = team(slot5, 1)
team6 = team(slot6, 1)
team7 = team(slot7, 1)
team8 = team(slot8, 1)
team9 = team(slot7, 2)
# team10 = team( ,3) # wrong position

demonThundeer = "demonThundeer.png"
diabloWater = "diabloWater.png"
greydemon = "greydemon.png"



#  -------------------------Define Function-------------------------
# Go to raid boss
def gotoRaid():
	if not exists(assist, 0):
		sysMsg("Going to raid event")
		if not exists(settings, 0):
			clkObj(home, 0, 1)
			wait(quest, long)
		clkObj(SPX, 0, 0, "Raid Menu")
	else:
		sysMsg("Already in raid menu")

# Refresh assist list if boss is already dead
def bossDead():
		sysMsg("Boss is already dead")
		clkObj(errDead)
		clkObj(assist)
		clkObj(refresh)
		sleep(normal)
		clkObj(closeX)

# Refresh assist list if raid is full (dummy)
def raidFull():
	sysMsg("Raid is full")
	pass

# Claim raid reward
def claimReward():
	sysMsg("Checking whether there is reward to be claimed")
	if exists(raidReward, 0):
		clkObj(raidReward)
		sleep(double)
		clkObj(cfnReward)
		if exists(addFd, changePage):
			clkObj(addFd, 0, 0, "Yes (add friend)")
			sleep(double)
		else:
			sysMsg("No assistant list found")
			sleep(normal)
	else:
		sysMsg("No reward found")


# After entering battle, toggle Auto if not On, and complete.
# Possible to add semi-auto strategy? 
def raidAction():
	sysMsg("Engaging raid boss")
	wait(btMenu, long)
	if exists(toggleAuto, normal):
		click(toggleAuto)
		sysMsg("Toggled auto")
		sleep(short)
		if pokLoad == 1:
			pokPugin.btQuest()
	else:
		sysMsg("Auto already on")
		if pokLoad == 1:
			pokPugin.btQuest()
	if exists(btEnd, battle):
		clkObj(btEnd)
		sleep(normal)
		mouseMove(50,0)
		click(atMouse())
		sysMsg("Raid completed")

def raidEnd():
	sysMsg("Skipping raid statistics")
	clkObj(atkDmg)
	clkObj(endMsg)	# Attack Damage, click, Accumulated Damage, click, Damage reward, Tier reward
	while exists(endMsg):			
		try:
			click(atMouse())
			mouseMove(10,0)
		except FindFailed:
			pass
	wait(home, long)
	sysMsg("Returned to raid menu")
	if exists(killed, normal):
		clkObj(killed, 0, 0, "OK (boss killed)")
	if exists(requestAid, 0):	# For main boss, check if still alive, and act accordingly.
		sysMsg("///// Main boss is still alive /////")
		q = 0
		clkObj(requestAid)
		clkObj(sendRequest)
		clkObj(sentRequest, 0, 0, "sentRequest")
		clkObj(back)
		while q != -1:
			sysMsg("Attempting to assist boss")
			raidAssist()
			clkObj(raidStart)
			sleep(double)
			if exists(killed):
				sysMsg("///// Main boss has been slain /////")
				q = -1
			else:
				sysMsg("///// Main boss is still alive /////")
				clkObj(back)
				q = q + 1
				sysMsg("/////Assisted " + str(q) + " time(s) /////")
			clkObj(killed, 0, 0, "OK (boss killed) #this line error?")
			sleep(normal)
	if exists(raidQuit, 0):	# For assisted boss, check if still alive, and act accordingly.
		sysMsg("///// Assisted boss is still alive /////")
		if raQuit == 0:
			clkObj(raidQuit)
			clkObj(raidQuited, 0, 0, "OK (quit assisting)")
		else:
			sysMsg("Waiting for " + str(raQuit) + " sec before status check or quit")
			if raQuit > 30:
				cd = raQuit
				while cd >= 0:
					sleep(cd)
					cd = cd - 30	# Check around every 30 sec to see if boss is still alive
					clkObj(back)
					clkObj(assist)
					if exists(killed, double):
						cd = -1	# Terminate the loop
			else:
				sleep(raQuit)
				clkObj(back)
				clkObj(assist)
			if exists(killed, double):
				sysMsg("///// Assisted boss has been slained /////")
				clkObj(killed, 0, 0, "OK (boss killed)")
				claimReward()
			else:
				clkObj(raidQuit)
				clkObj(raidQuited, 0, 0, "OK (quit assisting)")
	if exists(raidReward, 0):
		claimReward()

# Check for next area / reset raid message and act accordingly
def raidCleared():
	sysMsg("Checking if area is cleared")
	if exists(areaReward, 0):
		clkObj(areaReward)
		sleep(normal)
		if exists(nextArea):
			clkObj(nextArea, 0, 0, "Next Area")
			sysMsg("Going to next area")
		else:
			clkObj(reset)
			sysMsg("All area cleared. Resetting raid.")
	else:
		sysMsg("Area not cleared")

# Terminate command for insufficient RP
def raidBossEnd():
	clkObj(cancel)
	sysMsg("Insufficient RP")
	clkObj(back)
	clkObj(back)
	rBi = rB
	sleep(normal)
	sysMsg("Terminated command due to insufficient RP")

# Assist raid boss
def raidAssist(rA=1, PI=0):	# PI: As plugin - If 1, do not display end message based on local var
	rAi = 0
	sysMsg("Initializing RaidAssist command")
	gotoRaid()
	while rA > rAi:
		clkObj(assist)
		clkObj(aSlot1, normal, 0, "Assist List Slot 1")
		clkObj(okAssist, 0, 0, "OK (assist)")
		if exists(errDead, normal):
			bossDead()
		else:
			clkObj(raidStart)
			if exists(errDead, normal):
				bossDead()
			#teamSelect
			clkObj(btStart)
			if exists(errDead, normal):
				sysMsg("Assisted boss is already dead")
				bossDead()
			else:
				if exists(fullRaid, normal):
					raidFull()
				else:
					raidAction()
					raidEnd()
					rAi = rAi + 1
					if PI == 0:
						sysMsg("***************Assisted " + str(rAi) + " time(s)***************")

def raidBoss(rB=1, FF=0):	# FF: If 1, focus fire on existing boss. Team select not yet implemented.
	rBi = 0
	rAa = 0
	rRPi = resRP
	k = 0
	sysMsg("Initializing RaidBoss command")
	gotoRaid()
	while rB > rBi:
		clkObj(raidStart, 0, 0, "raidStart 1/2")	# on map screen
		sleep(normal)
		if exists(killed):
			sysMsg("Dead main boss found")
			clkObj(killed)
			sleep(normal)
		claimReward()
		raidCleared()
		if exists(requestedAid, 0):
			sysMsg("Existing boss found")
			if FF == 0:
				clkObj(back)
				while k == 0:
					sysMsg("Attampting to assist boss")
					raidAssist(rA=1, rB=1)
					rAa = rAa + 1
					sysMsg("/////Assisted " + str(rAa) + " time(s) /////")
					clkObj(raidStart)
					if exists(killed, double):
						sysMsg("///// Main boss has been slained /////")
						clkObj(killed, 0, 0, "OK (boss killed)")
						claimReward()
						areaCleared()
						rBi = rBi + 1
						k = 1
						sysMsg("*************** Successfully raided " + str(rBi) + " time(s) ***************")
					else:
						sysMsg("///// Main boss is still alive /////")
						clkObj(back)
			else:
				clkObj(raidStart, 0, 1, "raidStart 2/2")	# on boss menu
				# teamSelect(check boss type, choose correspondent team)
				clkObj(btStart)
				# RP check. If insufficient RP, restore RP or return to map screen as per settings.
				if exists(noRP, normal):
					if rRPi > 0:
						clkObj(confirm)
						clkObj(restoredRP)
						rRPi = rRPi - 1
						sysMsg("RP restored. Remaining " + str(rRPi) + " times before terminating the command")
						clkObj(btStart)
						raidAction()
						raidEnd()
						rBi = rBi + 1
						sysMsg("*************** Successfully raided " + str(rBi) + " time(s) ***************")
						raidCleared()
					else:
						raidBossEnd()
				else:
					raidAction()
					raidEnd()
					rBi = rBi + 1
					sysMsg("*************** Successfully raided " + str(rBi) + " time(s) ***************")
					raidCleared()
		else:
			clkObj(raidStart, 0, 1, "raidStart 2/2")	# on boss menu
			# teamSelect(check boss type, choose correspondent team)
			clkObj(btStart)
			# RP check. If insufficient RP, restore RP or return to map screen as per settings.
			if exists(noRP, normal):
				if rRPi > 0:
					clkObj(confirm)
					clkObj(restoredRP)
					rRPi = rRPi - 1
					sysMsg("///// RP restored. Remaining " + str(rRPi) + " times before terminating the command. /////")
					clkObj(btStart)
					raidAction()
					raidEnd()
					rBi = rBi + 1
					sysMsg("*************** Successfully raided " + str(rBi) + " time(s) ***************")
					raidCleared()
				else:
					raidBossEnd()
			raidAction()
			raidEnd()
			rBi = rBi + 1
			sysMsg("*************** Successfully raided " + str(rBi) + " time(s) ***************")
			raidCleared()
	else:
		if rB < 0:
			sysMsg("Error: rB must be empty or positive")
		else:
			sysMsg("*************** Command ended. Sleeping for" + str(changePage) + " sec ***************")
			sleep(changePage)




#  -------------------------Command-------------------------
raidBoss(rB=5)
raidAssist(rA=99)
raidBoss(rB=5)
raidAssist(rA=10)
raidBoss(rB=5)
raidAssist(rA=10)