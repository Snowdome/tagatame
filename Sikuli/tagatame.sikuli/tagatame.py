# tagatame.py last updated 26/06/2019

#  -------------------------Import Modules-------------------------
from sikuli import *
import time



#  -------------------------Settings-------------------------
Settings.MinSimilarity = 0.8


# Waiting time
short = 0.1
normal = 1
double = 2
changePage = 5
extend = 7
long = 180



#  -------------------------Assets-------------------------
# External
fiddler = "fiddler.png"


# Homepage
home = "home.png"
settings = "setting.png"
menuMain = "menuMain.png"
quest = Pattern("quest.png").similar(0.90)
questArrow = Pattern("bannerDown.png").similar(0.85)
SP = Pattern("spQuest.png").targetOffset(30,135)    # Location of Special Quest in respect to Secret Shop


# Battle menu
noQuota = "noQuota.png"
noAP = "noAP.png"
teamArrow = "teamArrow.png"
confirm = Pattern("confirm.png").similar(0.85)
btStart = Pattern("btStart.png").similar(0.75)


# Team slot (slot 8 not applicable to tower)
# Story and event team list stored separately
# Event includes Seiseki & Babel
# May also use png instead, but pay attention to similarity
slot1 = Pattern("teamArrow.png").targetOffset(80,60)    #Location(260, 240)
slot2 = Pattern("teamArrow.png").targetOffset(80,110)    #Location(260, 290)
slot3 = Pattern("teamArrow.png").targetOffset(80,160)    #Location(260, 340)
slot4 = Pattern("teamArrow.png").targetOffset(80,210)    #Location(260, 390)
slot5 = Pattern("teamArrow.png").targetOffset(80,260)    #Location(260, 440)
slot6 = Pattern("teamArrow.png").targetOffset(80,310)    #Location(260, 490)
slot7 = Pattern("teamArrow.png").targetOffset(80,360)    #Location(260, 540)
slot8 = Pattern("teamArrow.png").targetOffset(80,410)    #Location(260, 590)


# Battle
birdView = "birdView.png"
toggleAuto = "toggleAuto.png"
autoOn = "autoOn.png"
btMenu = "btMenu.png"
quitQuest = "quitQuest.png"
cfnQuit = Pattern("cfnQuit.png").similar(0.80)
btNext = "btNext.png"
questMission = "questMission.png"
visionMax = "visionMax.png"
questEnd = Pattern("questEnd.png").similar(0.80)

missionNew = "missionNew.png"
rewardGet = "rewardGet.png"



#  -------------------------Define Function-------------------------
# Debug message
def sysMsg(text):
    now = time.localtime()
    print("%02d:%02d:%02d " % (now.tm_hour, now.tm_min, now.tm_sec) + text)


# Click icon (optional: delay = length // loop = repeat until no longer exists)
def clkIco(icon, length=None, loop=False):
    if not exists(icon):
        sysMsg("Waiting for " + str(icon))
        wait(icon, FOREVER)
    if length != None:
        sysMsg("Delay clicking on " + str(icon) + " for length = " + str(length))
        sleep(length)
    if loop == False:
        click(icon)
        sysMsg("Clicked on " + str(icon))
    else:
        while exists(icon):
            click(icon)
            sleep(normal)
            sysMsg("Force clicking on " + str(icon))



# Wait for icon and press ESC (optional: delay = length)
def esc(icon, length=None):
    if not exists(icon, normal):
        wait(icon, FOREVER)
        sysMsg("Waiting for " + str(icon))
    if length is not None:
        sleep(length)
        sysMsg("Delay pressing ESC for " + str(icon) + " for length = " + str(length))
    type(Key.ESC)
    sysMsg("Pressed ESC for " + str(icon))
    sleep(normal)


# After entering battle, toggle Auto if not On, and complete.
def btAction():
    wait(btMenu, 20)
    if exists(toggleAuto, normal):
        click(toggleAuto)
        sysMsg("Toggled auto")
        sleep(short)
    else:
        sysMsg("Auto already on")
    clkIco(questMission)
    sysMsg("Quest completed")
    while exists(visionMax):
        sysMsg("Vision achieved")
        sleep(normal)
        esc(visionMax)
    else:    
        sleep(changePage)
        type(Key.ESC)


# After entering battle, quit.
def btQuit():
    click(btMenu)
    click(quitQuest)
    click(cfnQuit)


# Define class for story quest
class storyQ(object):
    def __init__(self, type, chapter, subChapter, stage):
        self.type = type    #main, seiseki, babel
        self.chapter = chapter
        self.subChapter = subChapter    #applicable to mainStory only
        self.stage = stage


# Define class for team
class team(object):
    def __init__(self, teamIco, teamSlot):
        self.teamIco = teamIco
        self.teamSlot = teamSlot


# Select team
def teamSelect(team):
    sysMsg("Changing team")
    if not exists(team.teamIco, normal):
        click(teamArrow)
        sleep(normal)
        click(team.teamSlot)
        sysMsg("Team changed")
    else:
        sysMsg("Team already chosen")

# Get reward from completed mission
def getReward():
    clkIco(menuMain)
    clkIco(missionNew)
    while exists(rewardGet):
        clkIco(rewardGet, None, True)
        sleep(normal)
        type(key.ESC)
    sysMsg("Done")