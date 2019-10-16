# event.py last updated 06/10/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
# Homepage
event = "event.png"
eventQuest = "eventQuest.png"
eventDaily = "eventDaily.png"


# Team
# s = selected team
# eT1s = Pattern("").similar(0.98)
# eT2s = Pattern("").similar(0.98)
# eT3s = Pattern("").similar(0.98)
# eT4s = Pattern("").similar(0.98)
# eT5s = Pattern("").similar(0.98)
# eT6s = Pattern("").similar(0.98)
eT7s = Pattern("eT7s.png").similar(0.98)
eT8s = Pattern("eT8s.png").similar(0.98)


# eT = event Team
# eT1 = team(eT1s, slot1)
# eT2 = team(eT2s, slot2)
# eT3 = team(eT3s, slot3)
# eT4 = team(eT4s, slot4)
# eT5 = team(eT5s, slot5)
# eT6 = team(eT6s, slot6)
eT7 = team(eT7s, slot7)
eT8 = team(eT8s, slot8)


# Wanted		#Currently not working
TS_VISION = "TS_VISION.png"


#  -------------------------Variables-------------------------
# Define class for event quest
class eventQ(object):
	def __init__(self, category, chapter, subChapter, stage):
		self.category = category	#seasonal, daily
		self.chapter = chapter
		self.subChapter = subChapter	#applicable to some daily quest only
		self.stage = stage

vision1CH = vc_cp_08
vision2CH = vc_cp_06
vision1 = eventQ("seasonal", vision1CH, 0, visionQ)
vision2 = eventQ("seasonal", vision2CH, 0, visionQ)


# Vision clear quest
vc_cp_06 = "vc_cp_06.png"
vc_cp_08 = "vc_cp_08.png"
visionQ =  "visionQ.png"


# Daily quest
dailyQuest = "dailyQuest.png"
goldQuest = "goldQuest.png"
goldQuestL4 = "goldQuestL4.png" # 0AP
goldQuestL3 = Pattern("goldQuestL4.png").targetOffset(0,106) # 0AP
goldQuestL2 = Pattern("goldQuestL4.png").targetOffset(0,212) # 0AP
goldQuestL1 = Pattern("goldQuestL4.png").targetOffset(0,288) # 0AP
gearQuest = "gearQuest.png"
gearQuestStg = "gearQuestStg.png"
gearQuestHard = "gearQuestHard.png"
gearQuestHardStg = "gearQuestHardStg.png"

goldL4 = eventQ("daily", goldQuest, 0, goldQuestL4)
goldL3 = eventQ("daily", goldQuest, 0, goldQuestL3)
goldL2 = eventQ("daily", goldQuest, 0, goldQuestL2)
goldL1 = eventQ("daily", goldQuest, 0, goldQuestL1)
gearL2 = eventQ("daily", gearQuestHard, 0, gearQuestHardStg)
gearL1 = eventQ("daily", gearQuest, 0, gearQuestStg)

# Weekly quest
weeklyVision = "weeklyVision.png"
weeklyVisionQ = "weeklyVisionQ.png"
weeklyGear = "weeklyGear.png"
weeklyGearQ = "weeklyGearQ.png"
weeklyItem = "weeklyItem.png"
weeklyItemQ = "weeklyItemQ.png"
weeklyMaterial = "weeklyMaterial.png"
weeklyMaterialQ = "weeklyMaterialQ.png"
weeklyGold = "weeklyGold.png"
weeklyGoldQ = "weeklyGoldQ.png"



#  -------------------------Define Function-------------------------
# Go to event quest
#def gotoEvent(eventQ):
#	if not exists(eventQ.title)
	
	
	if not exists(settings, short):
		click(home)
		wait(quest, 20)
		sleep(double)
	clkIco(quest)
	click(event)
	# For seasonal event
	if eventQ.category == "seasonal":
		sysMsg("Going to selected event quest stage")
		click(eventQuest)
		while not exists(eventQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(eventQ.chapter)
		while not exists(eventQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		click(eventQ.stage)
	# For daily quest
	if getattr(eventQ, "category") == "daily":
		sysMsg("Going to selected daily quest stage")
		click(eventDaily)
		while not exists(eventQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(eventQ.chapter)
		if not eventQ.subChapter == 0:	#untested
			while not exists(eventQ.subChapter, double):
				click(questArrow)
				sysMsg("Turning page: sub-chapter")
		click(chapter)
		while not exists(eventQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		click(eventQ.stage)		


# Auto restart until TS_VISION is found and used all quota
def tsVision(eventQ, team):
	sysMsg("Initializing tsVision command")
	if not exists(eventQ.stage, short):
		gotoEvent(eventQ)
	else:
		click(eventQ.stage)
	wait(teamArrow, changePage)
	teamSelect(team)
	clkIco(btStart)
	while not exists(noQuota, normal):
		if not exists(fiddler):
			sysMsg("Fiddler window not found!")
			popup("Fiddler window not found!")
			wait(fiddler, 60)
		wait(btMenu, 60)
		if exists(TS_VISION, normal):
			sysMsg("Target found")
			btAction()
		else:
			sysMsg("Target not found")
			btQuit()
		clkIco(eventQ.stage)
		clkIco(btStart)
	else:
		sysMsg("No more quota")
		type(Key.ESC) #return to Battle Preparation
		sleep(normal)
		type(Key.ESC) #return to Quest List
		sleep(double)
		clkIco(home) #return to Home page
		sleep(double)


#def dailyGold():
#	sysMsg("dailyGold started")
#	if not exists(goldQuestL4)
#		gotoEvent(goldL4. 




#  -------------------------Body-------------------------
# tsVision(vision1, eT7)
# tsVision(vision2, eT8)