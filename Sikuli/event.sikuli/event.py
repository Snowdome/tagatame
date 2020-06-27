# event.py last updated 24/05/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for special event
class evQ():
	def __init__(self, event, stat, stage, title):
		self.event = event
		self.stat = stat	# Current or Archive or Key or Daily event
		self.stage = stage
		self.title = title

#  -------------------------Assets-------------------------
evArchive = "evArchive.png"
access = "access.png"

#  -------------------------Variables-------------------------
halloween = evQ("halloweenEv.png", "Archive", "halloweenStage.png", "1589093890927.png")
wVday = evQ("whiteVdayEv.png", "Archive", "whiteVdayStage.png", "whiteVdayTitle.png")
vDay = evQ("vDayEv.png", "Archive", "vDayStage.png", "vDayTitle.png")
xmas = evQ("xmasEv.png", "Archive", "xmasStage.png", "xmasTitle.png")
harvestMoon = evQ("harvestMoonEv.png", "Archive", "harvestMoonStage.png", "harvestMoonTitle.png")
pirate = evQ("pirateEv.png", "Archive", "pirateStage.png", "pirateTitle.png")
easter = evQ("easterEv.png", "Archive", "easterStage.png", "easterTitle.png")
shieldBallon = evQ("1589098452707.png", "Current", "shieldBallonStage.png", "shieldBallonTitle.png")
xmas2018 = evQ("xmas2018Ev.png", "Archive", "xmas2018Stage.png", "xmas2018Title.png")
vDay2018 = evQ("vDay2018Ev.png", "Archive", "vDay2018Stage.png", "vDay2018Title.png")
halloween2018 = evQ("halloween2018Ev.png", "Archive", "halloween2018Stage.png", "halloween2018Title.png")
wrathArmorF = evQ("wrathArmorFEv.png", "Current", "wrathArmorFStage.png", "wrathArmorFTitle.png")
dWorld = evQ("dWorldEv.png", "Current", "dWorldStage.png", "dWorldTitle.png")
wedding = evQ("weddingEv.png", "Current", "weddingStage.png", "weddingTitle.png")
pipa = evQ(Pattern("pipaEv.png").targetOffset(425,35), "Key", "pipaStage.png", "pipaTitle.png")
starlight = evQ(Pattern("starlightEv.png").targetOffset(425,35), "Key", "starlightStage.png", "starlightTitle.png")
statue1 = evQ("1591547671751.png", "Daily", "1591547691756.png", Pattern("1591547706246.png").exact())
statue2 = evQ("1591547746528.png", "Daily", "1591547691756.png", Pattern("1591547777889.png").exact())
statue3 = evQ("1591547810713.png", "Daily", "1591547691756.png", Pattern("1591547828360.png").exact())
statue4 = evQ("1591547863076.png", "Daily", "1591547691756.png", Pattern("1591547875431.png").exact())
statue5 = evQ("1591547902442.png", "Daily", "1591547691756.png", Pattern("1591547927575.png").exact())
statue6 = evQ("1591547950399.png", "Daily", "1591547691756.png", Pattern("1591547961810.png").exact())


def gotoEv(evQ):
	if not exists(evQ.title, 0):
		sysMsg("Going to selected event")
		if not exists(evQ.stage, 0):
			if not exists(evQ.event, 0):
				if exists(home, 0):
					clkObj(mainMenu)
					clkObj(questLoc, remark="questLoc")
				else:
					clkObj(quest)
				clkObj(event, 0, daily)
				if evQ.stat == "Daily":
					clkObj(daily, 0, eventTitle)
					sleep(15)
					while not exists(evQ.event, double):
						clkObj(questArrow)
						sysMsg("Turning page: daily quest")
				else:
					if evQ.stat == "Key":
						clkObj(archive, 0, access)
						while not exists(evQ.event, double):
							clkObj(archivePageDown)
							sysMsg("Turning page: event archives")
					else:
						clkObj(eventQ, 0, eventTitle)
						sleep(15)
						if evQ.stat == "Archive":
							while not exists(evArchive, double):
								clkObj(questArrow)
								sysMsg("Turning page: main quest")
							clkObj(evArchive)
						while not exists(evQ.event, double):
							clkObj(questArrow)
							if evQ.stat == "Current":
								sysMsg("Turning page: main quest")
							if evQ.stat == "Archive":
								sysMsg("Turning page: archive quest")
			clkObj(evQ.event, 0, evQ.stage)
		clkObj(evQ.stage, 0, evQ.title)
	else:
		sysMsg("Already in selected event")

def autoAR(evQ, n=10):
	i = 0
	m = input("Enable merchantCheck? (1: Enable)", "1")
	sysMsg("m = " + str(m))
	if exists(arMenu):
		sysMsg("Ongoing auto repat found. Waiting for completion.")
		arCheck()
		merchantCheck(m)
		sleep(10)
		i = 1 + 1
	while i < n:
		gotoEv(evQ)
		enableAR()
		wait(settings, 30)
		arCheck()
		merchantCheck(m)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
		sleep(10)
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()

#  -------------------------Command-------------------------
#arCheck()
autoAR(wedding, 100)