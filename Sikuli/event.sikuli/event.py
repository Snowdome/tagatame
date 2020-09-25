# event.py last updated 22/09/2020

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
evAOT = "evAOT.png"
access = "access.png"

#  -------------------------Variables-------------------------
summer2020 = evQ("summer2020Ev.png", "Archive", "summer2020Stage.png", "summer2020Title.png")
halloween = evQ("halloweenEv.png", "Archive", "halloweenStage.png", "1589093890927.png")
wVday = evQ("whiteVdayEv.png", "Archive", "whiteVdayStage.png", "whiteVdayTitle.png")
vDay = evQ("vDayEv.png", "Archive", "vDayStage.png", "vDayTitle.png")
xmas = evQ("xmasEv.png", "Archive", "xmasStage.png", "xmasTitle.png")
harvestMoon = evQ("harvestMoonEv.png", "Archive", "harvestMoonStage.png", "harvestMoonTitle.png")
pirate = evQ("pirateEv.png", "Archive", "pirateStage.png", "pirateTitle.png")
easter = evQ("easterEv.png", "Archive", "easterStage.png", "easterTitle.png")
shieldBallon = evQ("1589098452707.png", "Current", "shieldBallonStage.png", "shieldBallonTitle.png")
xmas2018 = evQ("xmas2018Ev.png", "Archive", "xmas2018Stage.png", "xmas2018Title.png")
vDay2018 = evQ("vDay2018Ev.png", "Archive", "vDay2018Stage.png", "vDayy2018Title.png")
halloween2018 = evQ("halloween2018Ev.png", "Archive", "halloween2018Stage.png", "halloween2018Title.png")
wrathArmorF = evQ("wrathArmorFEv.png", "Current", "wrathArmorFStage.png", "wrathArmorFTitle.png")
dWorld = evQ("dWorldEv.png", "Current", "dWorldStage.png", "dWorldTitle.png")
wedding = evQ("weddingEv.png", "Current", "weddingStage.png", "weddingTitle.png")
AOT = evQ("AOTEvHard.png", "AOT", "AOTStage.png", "aotTitle.png")
AOT2 = evQ("AOTEvHell.png", "AOT", "AOT2Stage.png", "aot2Title.png")
yudit = evQ("yuditEv.png", "Current", "yuditStage.png", "yuditTile.png")

pipa = evQ(Pattern("pipaEv.png").targetOffset(425,35), "Key", "pipaStage.png", "pipaTitle.png")
starlight = evQ(Pattern("starlightEv.png").targetOffset(425,35), "Key", "starlightStage.png", "starlightTitle.png")
merchant = evQ(Pattern("merchantEv.png").targetOffset(435,40), "Key", "merchantStage.png", "merchantTitle.png")
statue1 = evQ("statue1.png", "Daily", "statueStage.png", Pattern("statue1Title.png").exact())
statue2 = evQ("statue2.png", "Daily", "statueStage.png", Pattern("statue2Title.png").exact())
statue3 = evQ("statue3.png", "Daily", "statueStage.png", Pattern("statue3Title.png").exact())
statue4 = evQ("statue4.png", "Daily", "statueStage.png", Pattern("statue4Title.png").exact())
statue5 = evQ("statue5.png", "Daily", "statueStage.png", Pattern("statue5Title.png").exact())
statue6 = evQ("statue6.png", "Daily", "statueStage.png", Pattern("statue6Title.png").exact())


def gotoEv(evQ):
	if not exists(evQ.title, 0):
		sysMsg("Going to selected event")
		if not exists(evQ.stage, 0):
			if not exists(evQ.event, 0):
				if exists(home, 0):
					clkObj(mainMenu)
					clkObj(questLoc, 0, event, remark="questLoc")
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
						if evQ.stat == "AOT":
							while not exists(evAOT, double):
								clkObj(questArrow)
								sysMsg("Turning page: main quest")
							clkObj(evAOT)
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

def evAR(evQ, n=10):
	i = 0
	if exists(arMenu):
		sysMsg("Ongoing auto repat found. Waiting for completion.")
		arCheck()
		sleep(10)
		i = 1 + 1
	while i < n:
		gotoEv(evQ)
		enableAR()
		waitObj(settings, 30)
		arCheck()
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)***************")
		sleep(10)
	if n < 0:
		sysMsg("Error: n must be empty or positive")
	else:
		exit()

#  -------------------------Command-------------------------
#arCheck()
#evAR(pirate, 50)
evAR(vDay, 30)