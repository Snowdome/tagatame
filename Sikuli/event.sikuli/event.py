# event.py last updated 13/05/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for special event
class evQ():
	def __init__(self, event, stat, stage, title):
		self.event = event
		self.stat = stat	# Current or Archive event
		self.stage = stage
		self.title = title

#  -------------------------Assets-------------------------
evArchive = "evArchive.png"

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
vDay2018 = evQ("1589384278969.png", "Archive", "1589384295853.png", "1589384308783.png")
halloween2018 = evQ("1589385170119.png", "Archive", "1589385194586.png", "1589385204403.png")
wrathArmorF = evQ("1589760714702.png", "Current", "1589760731470.png", "1589760751279.png")


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
				clkObj(event)
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
autoAR(wrathArmorF, 100)