# gift.py last updated 04/07/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
# Daily friend coin
menuFd = "menuFd.png"
fdGift = "fdGift.png"
giftGet = "giftGet.png"
giftGot = Pattern("giftGot.png").targetOffset(0,330)
giftTab = "giftTab.png"
giftSend = "giftSend.png"


# Draw menu
drawMenu = "drawMenu.png"
drawArrow = Pattern("drawLast.png").targetOffset(55,-44)
ticSum = "ticSum.png"
drawS1 = Pattern("drawLast.png").targetOffset(-165,-400)
drawS2 = Pattern("drawLast.png").targetOffset(-165,-275)
drawS3 = Pattern("drawLast.png").targetOffset(-165,-150)
drawS4 = Pattern("drawLast.png").targetOffset(-165,-25)
drawDown = Pattern("drawLast.png").targetOffset(-70,0)
max = "max.png"
skip = "skip.png"
drawOK =Pattern("drawOK.png").targetOffset(0,330)


# Inbox
sysGift = "sysGift.png"
giftWE = Pattern("giftWE.png").similar(0.75)	#With Expiry
openAll = "openAll.png"



#  -------------------------Define Function-------------------------
def sendGift():
	sysMsg("Initializing DaillyGift command")
	if not exists(settings, 0):
		click(home)
		sleep(changePage)
	clkIco(menuFd)
	clkIco(fdGift)
	clkIco(giftGet)
	clkIco(giftGot)
	clkIco(giftTab)
	clkIco(giftSend)
	sleep(changePage)
	type(Key.ESC)
	sleep(normal)


def drawTicket(box, n=1):	#slot = slot number or ticket name
	i = 0
	while i < n:
		if not exists(settings or ticSum, short):
			click(home)
			clkIco(drawMenu, double)
			sleep(double)
		while not exists(box, 0):
			clkIco(drawDown)
			sleep(normal)
		clkIco(box)
		clkIco(max)
		clkIco(confirm)
		clkIco(skip)
		clkIco(drawOK, double)
		i = i + 1
		sysMsg("Successfully executed " + str(i) + " time(s)")
	else:
		if n < 0:
			sysMsg("Error: n must be empty or positive")
		else:
			exit()


def getGift():
	sysMsg("Initializing GetGift command")
	i = 0
	if not exists(openAll, short):
		if not exists(giftWE, short):
			if not exists(settings, short):
				click(home)
			clkIco(sysGift, normal, True)
		clkIco(giftWE)
	while exists(openAll):
		while not exists(confirm):
			clkIco(openAll)
		clkIco(confirm)
		clkIco(drawOK)
		i = i + 1
		sysMsg("Successfully executed " + str(i) + " time(s)")
		sleep(normal)



#  -------------------------Variables-------------------------
ticGear = Pattern("ticGear.png").targetOffset(210,45)



#  -------------------------Body-------------------------
# sendGift()
# drawTicket(ticGear, 1)
getGift()