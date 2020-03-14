# feh.py last updated 08/03/2020
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
stage = 300
wTime = 10

i = 0
msgError = "Error: n must be empty or positive"
msgEnd = "***************End of command***************"

#  -------------------------Assets-------------------------
battle = "battle.png"
event = "event.png"
eventTitle = "eventTitle.png"
training = "training.png"
trainingTitle = Pattern("trainingTitle.png").targetOffset(0,370)
floor1 = "floor1.png"
floor2 = "floor2.png"
floor3 = "floor3.png"
floor4 = "floor4.png"
floor5 = "floor5.png"
floor6 = "floor6.png"
floor7 = "floor7.png"
floor8 = "floor8.png"
floor9 = "floor9.png"
floor10 = "floor10.png"

arena = "arena.png"
back = "back.png"

bonds = "bonds.png"
bondsTitle = "bondsTitle.png"
autoEq = "autoEq.png"
chooseStg = "chooseStg.png"

d3 = "d3.png"
d2 = "d2.png"
d1 = "d1.png"

refillAP = "refillAP.png"

btStart = "btStart.png"
btMenu = "btMenu.png"
toggleAuto = "toggleAuto.png"
toggleAutoOn = "toggleAutoOn.png"
stageCleared = "stageCleared.png"
gameover = "gameover.png"
surrender = "surrender.png"
done = "done.png"
bondSkip = "bondSkip.png"

#  -------------------------Define Function-------------------------
# Debug message
def sysMsg(text, popType=0):
	now = time.localtime()
	print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + text)
	if popType != 0:	# Sikilu pop up message
		decision = popAsk(text + "\nOr press No to terminate the command.", popType)
		now = time.localtime()
		if not decision:
			exit(1)
		print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + "Yes button has been pressed")

# Click object (optional: delay = length(sec), loop = 0/1/nextObject, remark = use customized message on log)
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
			if loop == 1:
				while exists(object):
					click(object)
					sleep(normal)
					mouseMove(10,0)
					sysMsg("Repeat clicking on " + subject)
			else:
				click(object)
				sleep(normal)
				while not exists(loop):
					sysMsg("Cannot find " + repr(loop))
					mouseMove(10,0)
					mouseMove(-10,0)
					click(atMouse())
					sysMsg("Repeat clicking on " + subject)
					sleep(normal)
	except FindFailed:
		sysMsg("Cannot find " + subject + "\nPress Yes to start the next step", "FindFailed Error")


def apCheck(option):
	if exists(refillAP):
		if option == 1:
			clkObj(refillAP)
			clkObj(done)
			sysMsg("AP has been refilled.")
		else:
			sysMsg("Insufficient AP. Terminating process.")
			exit()
	else:
		sysMsg("AP check passed")


def btAction(loop=0):
	wait(btMenu, long)
	clkObj(toggleAuto)
	clkObj(toggleAutoOn)
	sysMsg("Toggled auto")
	if exists(stageCleared, stage) or exists(gameover, stage):
		if exists(stageCleared, 0):
			sysMsg("Stage cleared")
		if exists(gameover, 0):
			sysMsg("Gameover")


def bondQ(d=d3, n=1, reAp=1):
	i = 0
	c = 0
	if exists(d, 0):
		decision = popAsk("Difficulties options found. Press yes to use current setup, \nOr press No to start all over.", "Waiting for decision")
		if not decision:
			sysMsg("No button has been pressed. Exiting to battle menu.")
			while not exists(battle, normal):
				clkObj(back)
			clkObj(battle)
			clkObj(event)
			clkObj(bonds)
			clkObj(chooseStg)
		else:
			sysMsg("Yes button has been pressed. Re-engaging battle.")
	else:
		if exists(bondsTitle, 0):
			sysMsg("Already in Forging Bonds quest menu.")
		else:
			sysMsg("Going to Forging Bonds quest menu.")
			clkObj(battle)
			clkObj(event)
			clkObj(bonds)
		clkObj(chooseStg)
	while i < n:
		clkObj(d)
		clkObj(btStart)
		apCheck(reAp)
		if exists(autoEq, normal):
			clkObj(autoEq)
		sleep(changePage)
		btAction()
		if exists(stageCleared):
			clkObj(stageCleared)
			clkObj(done)
			while exists(bondSkip, normal):
				clkObj(bondSkip)
				sleep(normal)
				while exists(done, normal):
					clkObj(done)
					sleep(normal)
			while exists(done, 0):
				clkObj(done)
				sleep(normal)
			i = i + 1
			c = c + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s); stage cleared " + str(c) + " time(s)***************")
		if exists(gameover):
			clkObj(surrender)
			i = i + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s); stage cleared " + str(c) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()

def trainQ(floor, n=1, reAp=0):
	i = 0
	c = 0
	if exists(trainingTitle, 0):
		sysMsg("Training Tower title found")
	else:
		while not exists(battle, normal):
			clkObj(back)
		clkObj(battle)
		clkObj(training)
	while not exists(floor):
		wheel(trainingTitle, Button.WHEEL_DOWN, 3)
	while i < n:
		clkObj(floor)
		clkObj(btStart)
		apCheck(reAp)
		sleep(changePage)
		btAction()
		if exists(stageCleared):
			clkObj(stageCleared)
			clkObj(done)
			while exists(done, 0):
				clkObj(done)
				sleep(normal)
			i = i + 1
			c = c + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s); stage cleared " + str(c) + " time(s)***************")
		if exists(gameover):
			clkObj(surrender)
			i = i + 1
			sysMsg("***************Successfully executed " + str(i) + " time(s); stage cleared " + str(c) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()
#  -------------------------Body-------------------------
#bondQ(n=50)
trainQ(floor4, n=5)