# worldBoss.py last updated 24/08/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

#  -------------------------Assets-------------------------
arrange = "arrange.png"
wbStart = "wbStart.png"

wbNext = "wbNext.png"
wbDmg = "wbDmg.png"
bottom = Pattern("bottom.png").targetOffset(-250,0)

#  -------------------------Define Function-------------------------
def worldBoss(n):
	i = 0
	while i < n:
		t = 0
		clkObj(arrange)
		clkObj(wbStart)
		apCheck(wbStart, q=2)
		sysMsg("Entered battle. Waiting for 100 sec.")
		sleep(100)
		while not exists(wbDmg):
			sysMsg("wbDmg not found. Waiting for 1 sec. Total waiting time = " + str(t) + " sec.")
			t = t + 1
			sleep(1)
		i = i + 1 
		clkObj(wbDmg)
		x = 0
		while not exists(arrange, 0):
			click(bottom)
			mouseMove(10,0)
			x = x + 1
			if x == 600:
				exit()
		sysMsg("Returned to world map. Successfully looped " + str(i) + " times.")

#  -------------------------Command-------------------------
worldBoss(999)