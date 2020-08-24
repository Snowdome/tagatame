# worldBoss.py last updated 24/08/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *

arrange = "arrange.png"
wbStart = "wbStart.png"

wbNext = "wbNext.png"
wbDmg = "wbDmg.png"


def worldBoss():
	t = 0
	n = 0
	clkObj(arrange)
	clkObj(wbStart)
	apCheck(wbStart)
	while not exists(wbNext):
		sysMsg("wbNext not found. Waiting for 10 sec. Total waiting time =" + str(t) + " sec.")
		t = t + 10
		sleep(10)
	n = n + 1
	sysMsg("wbNext found. Looped " + str(n) + " times.")

clkObj(wbStart)
apCheck(wbStart)