	   # video.py last updated 01/07/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


#  -------------------------Assets-------------------------
auto = "auto.png"
playNext = "playNext.png"
stopRec = "stopRec.png"

#  -------------------------Body-------------------------
if not exists(stopRec, 0):
	sysMsg("Please start recording first!")
	exit()
clkObj(playNext)
sysMsg("Start playing current section")
t = 0
while t != -1:
	if not exists(auto) and not exists(playNext):
		sleep(1)
		t = t + 1
		sysMsg("Auto button not found. Waiting for 1 more sec. Total waiting time: " + str(t) + " sec.")
	else:
		if exists(auto):
			t = -1
		if exists(playNext):
			sysMsg("Movie confirmation dialogue found.")
			clkObj(playNext)
			t = 0
clkObj(auto, 0)
i = 0
t = 0
while t != -1:
	if exists(home, 0):
		sysMsg("*************** End of chapter ***************")
		clkObj(stopRec)
		t = -1
	else:
		if exists(playNext, 0):
			i = i + 1
			t = 0
			sysMsg("*************** " + str(i) + " section(s) played ***************")
			clkObj(playNext)
			sleep(changePage)			
		else:
			t = t + refresh
			mouseMove(10,0)
			mouseMove(-10,0)
			sleep(refresh)
			sysMsg("End message not found. Waiting for " + str(refresh)+ " more sec. Total waiting time: " + str(t) + " sec.")