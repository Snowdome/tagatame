# raid.py last updated 04/07/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
assist = "assist.png"
guild = Pattern("guild.png").targetOffset(70,0)
friend = Pattern("friend.png").targetOffset(70,0)
anyone = "anyone.png"
refresh = "refresh.png" 
raidOK = "raidOK.png"
raidTeamSelect = "raidTeamSelect.png"
raidStart = "raidStart.png"
raidEnd = "raidEnd.png"
endMsg = "endMsg.png"
raidReward = Pattern("raidReward.png").similar(0.90)
cfnReward = Pattern("cfnReward.png").similar(0.80)
raidQuit = "raidQuit.png"
raidBack1 = "raidBack1.png"
raidBack2 =	 "raidBack2.png"
assistOngoing = Pattern("assistOngoing.png").similar(0.95)
assistFinished = Pattern("assistFinished.png").similar(0.95)
alreadyDead = Pattern("alreadyDead.png").targetOffset(0,255)
fullRaid = Pattern("fullRaid.png").targetOffset(0,255)
assistKilled = "assistKilled.png"
assistOK = "assistOK.png"
addFd = Pattern("addFd.png").targetOffset(0,380)


# Assist list
aSlot1 = Region(241,208,531,99)
joinSlot1 = Location(689, 271)
aSlot2 = Region(243,323,529,100)
joinSlot2 = Location(687, 386)



#  -------------------------Define Function-------------------------
# Define class for raid quest
class raidQ(object):
	def __init__(self, raidEvent, mode, timeout):
		self.event = "event"
		self.mode = "mode"		# 1. guild only / 2. friend only / 3. guild or friend / 4. anyone
		self.timeout = "timeout"	# how long until the withdraw from the assisted boss


# Go to raid boss
def gotoRaid(raidEvent):
	if not exists(settings, 0):
		click(home)
		wait(quest, 20)
		sleep(double)
	clkIco(raidEvent)


# Check if boss is already dead, and refresh if so


# Assist raid boss
		
#  -------------------------Variables-------------------------
# raidMF = "raidMF.png"
raidSSK = "raidSSK.png"
# Boss
chirstmasWind = "chirstmasWind.png"
queen = "queen.png"
demon = "demon.png"
waginao = "waginao.png"
orion = "orion.png"



#  -------------------------Body-------------------------
# raidAssist(raidQ)
SSK = raidQ(raidSSK, 4, FOREVER)
def raidAssist():
	sysMsg("Initializing RaidAssist command")
	clkIco(assist)
	sleep(double)
	click(joinSlot1)
	clkIco(raidOK)
	if exists(alreadyDead, normal):
		sysMsg("Boss is already dead")
		click(alreadyDead)
		click(assist)
		clkIco(refresh)
		sleep(normal)
		type(Key.ESC)
	else:
		clkIco(raidTeamSelect)
		clkIco(raidStart)
		if exists(alreadyDead, normal):
			sysMsg("Boss is already dead")
			click(alreadyDead)
			click(assist)
			clkIco(refresh)
			sleep(normal)
			type(Key.ESC)
		else:
			if exists(fullRaid, normal):
				sysMsg("Raid is full")
				click(fullRaid)
				sleep(normal)
				type(Key.ESC)
			else:
				sysMsg("Engaging raid boss")
				wait(raidEnd, 300)
				sysMsg("Battle ended")
				esc(raidEnd)
				sleep(5)
				esc(raidEnd)
				wait(endMsg)
				while exists(endMsg):
					sysMsg("Looping ending messages")
					sleep(3)
					click(endMsg)
					sleep(normal)
				else:
					if exists(assistKilled, normal):
						click(assistOK)
					else:
						sysMsg("ended")
						clkIco(raidReward)
						clkIco(cfnReward)
						clkIco(addFd)
					clkIco(raidReward)
					clkIco(cfnReward)
					clkIco(addFd)	




#  -------------------------Command-------------------------
while True:
	raidAssist()



#  -------------------------Ideas-------------------------
# 1. Set assist mode (1:guild only / 2:friend only / 3:guild or friend / 4:anyone
# 2. Set ongoing mode (A: keep / B: skip after (n) second)
# 3. Choose boss, Start raid, wait until auto end, OK x3 (or 4 if boss is dead)
# 4. If boss dead, raidOK, raidReward x2, raidOK
# 5A. For mode A. if boss alive, refresh once per minute, then step 3
# 6A. Repeat step 3
# 5B. For mode B, if boss alive, raidBack1, wait (n) second, assist_onhoing
# 6B. If raidQuit exist, raidQuit, else raidReward
# 7B. Repeat step 3