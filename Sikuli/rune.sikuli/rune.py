# rune.py last updated 07/03/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


#  -------------------------Assets-------------------------
enhance = "enhance.png"
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
		clkObj(enhance, 0, eventTitle)
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

#  -------------------------Body-------------------------
#set:	1 物攻 / 2 魔攻 / 3 物防 / 4 魔防 / 5 HP
#slot:	1 物攻器用 / 2 物防物防 / 3 HP / 4 魔攻器用 / 5 魔防運 / 6 素早
runeQ(set3, slot5, d3, 20)