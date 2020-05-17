# rune.py last updated 10/05/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


#  -------------------------Assets-------------------------
set1 = "set1.png"	# 物攻+10%
set2 = "set2.png"	# 魔攻+10%
set3 = "set3.png"	# 物防+10%
set4 = "set4.png"	# 魔防+10%
set5 = "set5.png"	# HP+15%
slot1 = "slot1.png"	# 物攻/器用
slot2 = "slot2.png"	# 物防/会心
slot3 = "slot3.png"	# HP
slot4 = "slot4.png"	# 魔攻/器用
slot5 = "slot5.png"	# 魔防/運
slot6 = "slot6.png"	# 素早
d1 = "d1.png"
d2 = "d2.png"
d3 = "d3.png"
enhance = "enhance.png"
evolve = "evolve.png"
enhanceTitle = Pattern("enhanceTitle.png").targetOffset(85,380)	# Loc of enhance button in respect to the title bar
evolveTitle = Pattern("evolveTitle.png").targetOffset(85,380)	# Loc of enhance button in respect to the title bar
enSuccess = "enSuccess.png"
enFail = "enFail.png"
done = "done.png"
gaugeRdy = Pattern("gaugeRdy.png").similar(0.90)
gaugeUse = "gaugeUse.png"
statChange = "statChange.png"
statChangeTitle = Pattern("statChangeTitle.png").targetOffset(0,182)	# Loc of enhance button in respect to the title bar
statChangeConfirm  = "1589088541580.png"
stat25 = Pattern("stat25.png").exact()
evoB10 = Pattern("evoB10.png").exact()
evoC10 = Pattern("evoC10.png").exact()

# Go to special event (set, slot, d=difficulty)
def gotoRuneQ(set, slot, d):
	sysMsg("Going to selected rune quest")
	if not exists(eventTitle, 0):
		if exists(home, 0):
			clkObj(mainMenu)
			clkObj(questLoc, remark="questLoc")
		else:
			clkObj(quest)
		clkObj(event)
		clkObj(daily, 0, eventTitle)
	while not exists(set, double):
		clkObj(questArrow)
		sysMsg("Turning page: enhance quest")
	clkObj(set)
	while not exists(slot, double):
		clkObj(questArrow)
		sysMsg("Turning page: enhance quest")
	clkObj(slot)
	clkObj(d)
	sysMsg("Arrived selected rune quest")

def runeQ(set, slot, d=d3, n=1):
	sysMsg("Initializing Auto Rune command")
	i = 0
	if exists(btAgain):
		decision = popAsk("Re-battle button found. Press yes to use current setup, \nOr press No to start all over.", "Waiting for decision")
		if not decision:
			sysMsg("No button has been pressed. Exiting to home menu.")
			clkObj(btEnd)
			gotoRuneQ(set, slot, d)
		else:
			sysMsg("Yes button has been pressed. Re-engaging battle.")
			clkObj(btAgain)
			mouseMove(10,0)
			mouseMove(-10,0)
			click(atMouse())
	else:
		gotoRuneQ(set, slot, d)
	clkObj(btStart)
	apCheck(btStart, q=3)
	runeCheck()
	btAction(loop=1)
	i = i + 1
	sysMsg("***************Successfully executed for the 1st time***************")
	while i < n:
		clkObj(btAgain)
		mouseMove(10,0)
		mouseMove(-10,0)
		click(atMouse())
		apCheck(btAgain, q=3)
		clkObj(btStart)
		runeCheck()
		btAction(loop=1)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()

def gaugeCheck():
	if exists(gaugeRdy, 0):
		sysMsg("Gauge bar has been filled. Proceed using gauge for next enhancement.")
		clkObj(gaugeUse)
	else:
		sysMsg("Gauge bar is not full yet.")

def runeEnh():
	n = int(input("Number of successful enhancement:", "3"))
	#evo = int(input("Current rune's evolve level:", "0"))
	enh = int(input("Current rune's enhancement level:", "0"))
	sysMsg("Initializing runeEnhance. Given rune input: evo = " + str(evo) + ", enh = " + str(enh))
	i = 0
	f = 0
	if not exists(enhanceTitle, 0):
		if exists(enhance):
			clkObj(enhance)
		else:
			sysMsg("Not in rune menu.")
			exit()
	clkObj(enhanceTitle)
	clkObj(confirm)
	while i < n:
		if enh != 3:
			t = 0
			while not exists(enSuccess, 0) and not exists(enFail, 0):
				sysMsg("Waiting for enhance result. Total waiting time: " + str(t) + " sec.")
				wait(1)
				t = t + 1
			else:
				if exists(enSuccess, 0):
					enh = enh + 1
					i = i + 1
					sysMsg("Enhance succeed.")
					if enh != 3:
						clkObj(enhance)
						clkObj(confirm)
						while exists(enSuccess, 0):
							sleep(1)
					else:
						clkObj(done)
				if exists(enFail, 0):
					f = f + 1
					sysMsg("Enhance failed. Total failed attempt: " + str(f) + " times.")
					wait(enhance)
					gaugeCheck()
					clkObj(enhance)
					clkObj(confirm)
					while exists(enFail, 0):
						sleep(1)
		else:
			clkObj(evolve)
			clkObj(evolveTitle)
			clkObj(confirm)
			clkObj(done)
			#evo = evo + 1
			enh = 0
			sysMsg("Rune evolved.")

def runeRe3():
	i = 0
	if not exists(statChangeTitle, 0):
		if exists(statChange):
			clkObj(statChange)
		else:
			sysMsg("Not in rune menu.")
	clkObj(statChangeTitle)
	sleep(0.5)
	while not exists(stat25, 0):
		clkObj(statChangeConfirm)
		clkObj(confirm)
		i = 1 + 1
		if not exists(stat25):
			sysMsg("Total attempts: " + str(i) + " times")
			sysMsg("Refreshed but not at maximum, continue?", "Waiting for decision")
	else:
		sysMsg("Error - basic stat already at maximum.")
		exit()


#  -------------------------Body-------------------------
#set:	1 物攻 / 2 魔攻 / 3 物防 / 4 魔防 / 5 HP
#slot:	1 物攻器用 / 2 物防物防 / 3 HP / 4 魔攻器用 / 5 魔防運 / 6 素早
#runeQ(set3, slot5, d3, 20)
#runeEnh()
runeRe3()