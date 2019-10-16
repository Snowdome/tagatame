# inspSkill.py last updated 04/07/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *

#  -------------------------Assets-------------------------
# Homepage
menuEq = "menuEq.png"
tabIS = Pattern("ISTab.png").similar(0.80)
nextPage = "nextPage.png"
resetTab = "resetTab.png"
resetBtn = Pattern("resetBtn.png").similar(0.80)
resetOK = Pattern("resetOK.png").similar(0.80)


# Battle
learnIS = "learnIS.png"
btAgain = "btAgain.png"


# Skill
OHS300 = "1hs300.png"
staff140 = "staff140.png"
staff200 = "staff200.png"
staff210 = staff140
staff240 = "staff230.png"
staff231 = ""
staff231A = ""
staff331 = "staff331.png"



#  -------------------------Define Function-------------------------
def gotoQuest():
	click(home)
	tagatame.clkIco(quest)
	click(story)
	#click(mainStory)
	click(seiseki)
	while not exists(bannerCh, 1.2):
		click(questDown)
		print("Turning page: chapter")
	click(bannerCh)
	while not exists(bannerStg, 1.2):
		click(storyDown)
		print("Turning page: stage")
	click(bannerStg)
	

def resetEQ(EQ):
	click(menuMain)
	click(menuEq)
	click(tabIS)
	while not exists(EQ, 1):
		click(nextPage)
		print("Turning page: gear")
	click(EQ)
	click(resetTab)
	click(resetBtn)
	click(resetOK)
	click(home)
	sleep(1)
	gotoQuest()
	

def btActionIS():
	sysMsg("Initializing btActionIS command")
	while True:
		click(btStart)
		if exists(cfnEmpty):
			click(cfnEmpty)
		wait(btMenu, 20)
		if exists(toggleAuto, normal):
			click(toggleAuto)
			sleep(short)
		clkIco(questMission)
		if exists(learnIS, changePage):
			if exists(targetIS):
				click(learnIS)
				click(btAgain)
				print("Target IS found - entering battle again")	
			else:
				if exists(finalIS):
					popup("Final Inspiration Skill learnt")
					exit()
				else:
					click(learnIS)
					tagatame.esc(questEnd)
					print("Wrong IS learnt - resetting IS")
					resetEQ1()
		else:
			click(btAgain)
			sleep(normal)
			click(btAgain)
			print("No IS learnt - entering battle again")
		


#  -------------------------Variables-------------------------
chapter = "chapter.png"
stage = Pattern("stage.png").similar(0.80)
#EQ1 = Pattern("eq1.png").similar(0.96)
EQ1 = Pattern("EQ1.png").similar(0.90)
targetIS = staff200 #and staff230
#finalIS = staff230



#  -------------------------Body-------------------------
resetEQ(EQ1)
# btActionIS()