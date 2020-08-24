# worldBoss.py last updated 24/08/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

arrange = "arrange.png"
wbStart = "wbStart.png"

wbNext = "wbNext.png"
wbDmg = "wbDmg.png"
bottom = Pattern("bottom.png").targetOffset(-250,0)

def worldBoss(n):
	i = 0
	while i < n:
		t = 0
		clkObj(arrange)
		clkObj(wbStart)
		apCheck(wbStart)
		sleep(80)
		while not exists(wbDmg):
			sysMsg("wbNext not found. Waiting for 1 sec. Total waiting time = " + str(t) + " sec.")
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

worldBoss(999)