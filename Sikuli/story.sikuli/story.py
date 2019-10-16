# story.py last updated 18/06/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
seiseki = "seiseki.png"
babel = "babel.png"
babelBanner = "babelBanner.png"



#  -------------------------Define Function-------------------------
# Define class for story quest
class storyQ(object):
	def __init__(self, type, chapter, subChapter, stage):
		self.type = type	#main, seiseki, babel
		self.chapter = chapter
		self.subChapter = subChapter	#applicable to mainStory only
		self.stage = stage


# Go to story quest
def gotoStory(storyQ):
	if not exists(settings, short):
		click(home)
		wait(quest, 20)
		sleep(double)
	clkIco(quest)
	click(story)
	# For main story
	if storyQ.type == "main":
		sysMsg("Going to selected story stage")
		click(mainStory)
		sleep(changePage)
		type(Key.ESC)	#return to sub-chapter list
		sleep(normal)
		type(Key.ESC)	#return to chapter list
		sleep(normal)
		while not exists(storyQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(storyQ.chapter)
		while not exists(storyQ.subChapter, double):
			click(questArrow)
			sysMsg("Turning page: sub-chapter")
		click(storyQ.subChapter)
		while not exists(storyQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		click(storyQ.stage)
	# For Seiseki no Tsuioku
	if storyQ.type == "seiseki":
		sysMsg("Going to selected Seiseki no Tsuioku stage")
		click(seiseki)
		sleep(changePage)
		while not exists(storyQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(storyQ.chapter)
		while not exists(storyQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		click(storyQ.stage)
	# For Babel Chronicle
	if storyQ.type == "babel":
		sysMsg("Going to selected Babel Chronicle stage")
		click(babel)
		clkIco(babelBanner)
		while not exists(storyQ.chapter, double):
			click(questArrow)
			sysMsg("Turning page: chapter")
		click(storyQ.chapter)
		while not exists(storyQ.stage, double):
			click(questArrow)
			sysMsg("Turning page: stage")
		click(storyQ.stage)



#  -------------------------Command-------------------------
# (empty)