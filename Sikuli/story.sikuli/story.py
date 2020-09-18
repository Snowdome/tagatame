# story.py last updated 16/09/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for story quest
class storyQ(object):
	def __init__(self, type, chapter, subChapter, stage):
		self.type = type	#main, seiseki, babel
		self.chapter = chapter
		self.subChapter = subChapter	#applicable to mainStory only
		self.stage = stage


#  -------------------------Assets-------------------------
mainStory = "mainStory.png"
mainStoryBack = "mainStoryBack.png"
mainStory1 = "mainStory1.png"
mainStoryI = "mainStoryI.png"
mainStory2 = "mainStory2.png"
chLoc1 = Pattern("mainMenu.png").targetOffset(-180,150)	# Location of 1st chapter in respect to the menu button
chLoc2 = Pattern("mainMenu.png").targetOffset(-180,260)	# Location of 2nd chapter in respect to the menu button
chLoc3 = Pattern("mainMenu.png").targetOffset(-180,370)	# Location of 3rd chapter in respect to the menu button
chLoc4 = Pattern("mainMenu.png").targetOffset(-180,480)	# Location of 4th chapter in respect to the menu button
chLocS1 = Pattern("mainMenu.png").targetOffset(-180,130)	# Location of 1st sub-chapter in respect to the menu button
chLocS2 = Pattern("mainMenu.png").targetOffset(-180,220)	# Location of 2nd sub-chapter in respect to the menu button
chLocS3 = Pattern("mainMenu.png").targetOffset(-180,330)	# Location of 3rd sub-chapter in respect to the menu button
chLocS4 = Pattern("mainMenu.png").targetOffset(-180,430)	# Location of 4th sub-chapter in respect to the menu button
seiseki = "seiseki.png"
babel = "babel.png"
babelBanner = "babelBanner.png"

ss10Ex = storyQ("seiseki", "ss10ExCh.png", 0, "ss10ExStage.png")

#  -------------------------Define Function-------------------------
# Go to story quest
def gotoStory(storyQ):
	s = storyQ.subChapter
	if not exists(settings, short):
		clkObj(home)
		waitObj(quest, 20)
		sleep(double)
	clkObj(quest, loop=story)
	clkObj(story)
	# For main story
	if storyQ.type == "main":
		sysMsg("Going to selected story stage")
		clkObj(mainStory, loop=mainStoryBack)
		if storyQ.chapter < 5:
			clkObj(mainStory1)
			if storyQ.chapter == 1:
				clkObj(chLoc4, remark="Chapter 1")
			elif storyQ.chapter == 2:
				clkObj(chLoc3, remark="Chapter 2")
			elif storyQ.chapter == 3:
				clkObj(chLoc2, remark="Chapter 3")
			else:
				clkObj(chLoc1, remark="Chapter 4")
		elif storyQ.chapter == "i":
			clkObj(mainStoryI)
			clkObj(chLoc1, remark="Interlude")
			s = 4
		else:
			clkObj(mainStory2)
			if storyQ.chapter == 5:
				clkObj(chLoc2, remark="Chapter 5")
			else:
				clkObj(chLoc1, remark="Chapter 6")
		while s > 4:
			clkObj(questArrow)
			s = s - 4
			sysMsg("Turning page: sub-chapter")
			sleep(2)
		if s == 4:
			clkObj(chLocS1)
		elif s == 3:
			clkObj(chLocS2)
		elif s == 2:
			clkObj(chLocS3)
		else:
			clkObj(chLocS4)
		while not exists(storyQ.stage, double):
			clkObj(questArrow)
			sysMsg("Turning page: stage")
		clkObj(storyQ.stage)
	
	# For Seiseki no Tsuioku
	if storyQ.type == "seiseki":
		sysMsg("Going to selected Seiseki no Tsuioku stage")
		clkObj(seiseki, loop=eventTitle)
		sleep(10)
		while not exists(storyQ.chapter, double):
			clkObj(questArrow)
			sysMsg("Turning page: chapter")
		clkObj(storyQ.chapter)
		while not exists(storyQ.stage, double):
			clkObj(questArrow)
			sysMsg("Turning page: stage")
		clkObj(storyQ.stage)
	
	# For Babel Chronicle
	if storyQ.type == "babel":
		sysMsg("Going to selected Babel Chronicle stage")
		clkObj(babel)
		clkObj(babelBanner)
		while not exists(storyQ.chapter, double):
			clkObj(questArrow)
			sysMsg("Turning page: chapter")
		clkObj(storyQ.chapter)
		while not exists(storyQ.stage, double):
			clkObj(questArrow)
			sysMsg("Turning page: stage")
		clkObj(storyQ.stage)

def storyAR(storyQ, n=10):
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
		gotoStory(storyQ)
		enableAR()
		waitObj(settings, 30)
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
# (empty)
storyAR(ss10Ex, 20)