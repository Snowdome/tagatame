# spEvent.py last updated 07/07/2019

#  -------------------------Import Modules-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
bossHard = Pattern("bossHard.png").similar(0.88)
spStart = "spStart.png"
spDrawBtn = "spDrawBtn.png"
spDraw10 = Pattern("spDraw10.png").similar(0.96)
empty = "empty.png"
noCoin = "noCoin.png"
spOK = "drawOK.png"

#  -------------------------Variables-------------------------
# Define class for special event

class spQ(object):
    def __init__(self, event, logo, stage, reward):
        self.event = event
        self.logo = logo
        self.stage = stage
        self.reward = reward

movie1Ev = "movie1Ev.png"
movie1Logo = "movie1Logo.png"
movie1Stage = "movie1Stage.png"
movie1Coin = "movie1Coin.png"
movie1 = spQ(movie1Ev, movie1Logo, movie1Stage, movie1Coin)


movie2Ev = "movie2Ev.png"
movie2Logo = "movie2Logo.png"
movie2Stage = "movie2Stage.png"
movie2Coin = "movie2Coin.png"
movie2 = spQ(movie2Ev, movie2Logo, movie2Stage, movie2Coin)


movie3Ev = "movie3Ev.png"
movie3Logo = "movie3Logo.png"
movie3Stage = "movie3Stage.png"
movie3Coin = "movie3Coin.png"
movie3 = spQ(movie3Ev, movie3Logo, movie3Stage, movie3Coin)


fggEv = "fggEv.png"
fggLogo = "fggLogo.png"
fggStage = "fggStage.png"
fggCoin = "fggCoin.png"
fgg = spQ(fggEv, fggLogo, fggStage, fggCoin)

dramaEv = "dramaEv.png"
dramaLogo = "dramaLogo.png"
dramaStage = "dramaStage.png"
dramaCoin = "dramaCoin.png"
drama = spQ(dramaEv, dramaLogo, dramaStage, dramaCoin)



#  -------------------------Define Function-------------------------
# Go to special event
def gotoSP(spQ):
    if not exists(spQ.stage, short):
        sysMsg("Going to selected special event")
        if not exists(spQ.logo, short):
            if not exists(spQ.event, short):
                if exists(home, short):
                    click(home)
                clkIco(SP, None, True)
                while not exists(spQ.event, double):
                    click(questArrow)
                    clkIco(spQ.event)
            clkIco(bossHard)
        clkIco(spStart)
    else:
        sysMsg("Already in selected special event")


# After entering battle, toggle Auto if not On, and complete.
def spAction(reward):
    wait(btMenu, 20)
    if exists(toggleAuto, normal):
        click(toggleAuto)
        sysMsg("Toggled auto")
        sleep(short)
    else:
        sysMsg("Auto already on")
    wait(reward, FOREVER)
    if exists(spStart):
        sysMsg("Quest failed")
    else:
        sysMsg("Quest completed")
        clkIco(reward)
        global c
        c = c + 1


# Start battle - hard boss
def spBoss(spQ, n=1):
    sysMsg("Initializing SpecialEventBoss command")
    i = 0
    global c
    c = 0
    if not exists(spQ.reward, short):
        gotoSP(spQ)
        clkIco(bossHard)
    while i < n:
        clkIco(spStart)
        #teamSelect(team)
        clkIco(btStart)
        spAction(spQ.reward)
        i = i + 1
        sysMsg("Successfully executed " + str(i) + " time(s); killed boss " + str(c) + " time(s)")
        sleep(normal)
    else:
        if n < 0:
            sysMsg("Error: n must be empty or positive")
        else:
            exit()


def spDraw(spQ, n=1):
    sysMsg("Initializing SpecialEventDraw command")
    i = 0
    if spQ != "now":
        gotoSP(spQ)
        clkIco(spDrawBtn)
    clkIco(spDraw10, None, True)
    if exists(empty, short):
        clkIco(spOK, None, True)
        clkIco(spDraw10, None, True)
    click(atMouse())
    i = i + 1
    sysMsg("Successfully executed 1st time")
    if n == "all":
        while not exists(noCoin):
            click(atMouse())
            if exists(empty):
                clkIco(spOK, None, True)
                clkIco(spDraw10, None, True)
            i = i + 1
            sleep(extend)
            sysMsg("Successfully executed " + str(i) + " times")
            if exists(noCoin):
                exit()
    else:
        while i < n:
            click(atMouse())
            if exists(empty):
                clkIco(spOK, None, True)
                clkIco(spDraw10, None, True)
            i = i + 1
            sleep(extend)
            sysMsg("Successfully executed " + str(i) + " times")
        else:
            if n < 0:
                sysMsg("Error: n must be empty or positive")
            else:
                exit()



#  -------------------------Command-------------------------
# spBoss(movie1, 5)
# spBoss(movie2, 6)
# spBoss(fgg, 5)
spDraw("now", "all")
# spDraw(movie1, 50)
# spDraw(movie2, 50)
# spDraw(fgg, 50)
# spBoss(drama, 8)