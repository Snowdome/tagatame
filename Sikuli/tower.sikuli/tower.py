# tower.py last updated 07/07/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
#Interface
challenge = "challenge.png"
tower = "tower.png"
veda = "veda.png"
extra = "extra.png"
mobius = "mobius.png"
towerStart = "towerStart.png"
invalid = Pattern("invalid.png").targetOffset(0,250)
reward = "reward.png"


#Team
#s = selected team
tT1s = Pattern("tT1s.png").exact()
tT2s = Pattern("tT2s.png").exact()
tT3s = Pattern("tT3s.png").exact()
tT4s = Pattern("tT4s.png").exact()
tT5s = Pattern("tT5s.png").exact()
tT6s = Pattern("tT6s.png").exact()
tT7s = Pattern("tT7s.png").exact()


#tT = tower Team
tT1 = team(tT1s, slot1)
tT2 = team(tT2s, slot2)
tT3 = team(tT3s, slot3)
tT4 = team(tT4s, slot4)
tT5 = team(tT5s, slot5)
tT6 = team(tT6s, slot6)
tT7 = team(tT7s, slot7)



#  -------------------------Define Function-------------------------
# Go to tower menu
def gotoTower(type):
    if not exists(towerStart, 0):
        sysMsg("Going to selected tower (start floor menu)")
        if not exists(type):
            if exists(home, 0):
                clkIco(home)
            clkIco(quest, None, True)
            clkIco(challenge, None, True)
            clkIco(tower, None, True)
        # In case there are more towers
        # while not exists(type, short):
            # click(questArrow)
            # sysMsg("Turning page: tower")
        clkIco(type)
        clkIco(towerStart)
    else:
        sysMsg("Already in selected tower (start floor menu)")


# Choose team to enter tower and toggle auto (if not already on)
def autoTower(team):
    i = 0
    sysMsg("Initializing AutoTower command")
    if not exists(btStart, 0):
        gotoTower(veda)
    teamSelect(team)
    while not exists(invalid):
        click(btStart)
        if exists(invalid, normal):
            click(invalid)
            sysMsg("Invalid team composition")
        else:    
            wait(btMenu, 20)
            if exists(toggleAuto, normal):
                click(toggleAuto)
                sysMsg("Toggled auto")
                sleep(short)
            else:
                sysMsg("Auto already on")
            wait(reward or towerStart, FOREVER)
            if exists(reward):
                i = i + 1
                sysMsg(str(i) + " floor(s) cleared")
                click(reward)
                esc(reward)
                esc(questEnd)
                sleep(changePage)
                clkIco(towerStart)
            else:
                sysMsg("Returned to Battle Preparation")
                sleep(changePage)

#  -------------------------Variables-------------------------



#  -------------------------Command-------------------------
autoTower(tT1)
autoTower(tT2)
autoTower(tT3)
autoTower(tT4)
autoTower(tT5)
autoTower(tT6)
autoTower(tT7)