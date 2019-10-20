# spEvent.py last updated 20/10/2019

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *



#  -------------------------Assets-------------------------
bossHard = "bossHard.png"
bossHardX = "bossHardX.png"
spStart = "spStart.png"
evDraw = "evDraw.png"
evDrawX = "evDrawX.png"
evDraw10 = Pattern("evDraw10.png").targetOffset(115,415)	# Location in respect to the title bar
empty = "empty.png"
noCoin = Pattern("noCoin.png").targetOffset(0,240)	# Location of OK button in respect to the message
spOK = "spOK.png"
drawing = "drawing.png"

#  -------------------------Variables-------------------------
# Define class for special event

class spQ(object):
	def __init__(self, event, menuLoc, logo, stage, reward):
		self.event = event
		self.menuLoc = menuLoc	# up: Above news banner	left: On the left of news banner
		self.logo = logo
		self.stage = stage
		self.reward = reward

# Advance Boss Movie01 - 「劇場版 誰ガ為のアルケミスト」前編
movie1Ev = "movie1Ev.png"
movie1Logo = "movie1Logo.png"
movie1Stage = "movie1Stage.png"
movie1Coin = "movie1Coin.png"
movie1 = spQ(movie1Ev, "up", movie1Logo, movie1Stage, movie1Coin)

# Advance Boss Movie02 - 「劇場版 誰ガ為のアルケミスト」中編
movie2Ev = "movie2Ev.png"
movie2Logo = "movie2Logo.png"
movie2Stage = "movie2Stage.png"
movie2Coin = "movie2Coin.png"
movie2 = spQ(movie2Ev, "up", movie2Logo, movie2Stage, movie2Coin)

# Advane Boss Movie03 - 「劇場版 誰ガ為のアルケミスト」後編
movie3Ev = "movie3Ev.png"
movie3Logo = "movie3Logo.png"
movie3Stage = "movie3Stage.png"
movie3Coin = "movie3Coin.png"
movie3 = spQ(movie3Ev, "up", movie3Logo, movie3Stage, movie3Coin)

# Advance Boss 3Title - すなわち恋の雪景色
fggEv = "fggEv.png"
fggLogo = "fggLogo.png"
fggStage = "fggStage.png"
fggCoin = "fggCoin.png"
fgg = spQ(fggEv, "up", fggLogo, fggStage, fggCoin)

# Advance Boss Butai - 誓いの刃、貫く魔槍
dramaEv = "dramaEv.png"
dramaLogo = "dramaLogo.png"
dramaStage = "dramaStage.png"
dramaCoin = "dramaCoin.png"
drama = spQ(dramaEv, "up", dramaLogo, dramaStage, dramaCoin)

# Advance Boss Novel - 姉弟とヒトリの剣士
# Missing

# Advnace Boss Templar - 七色琥珀のサンセリフ
# Missing

# Advance Boss Crossover - 夜明けに奏でるクレーデレ
sevenSinEv = "7sinEv.png"
sevenSinLogo = "7sinLogo.png"
sevenSinStage = "7sinStage.png"
sevenSinCoin = "7sinCoin.png"
sevenSin = spQ(sevenSinEv, "left", sevenSinLogo, sevenSinStage, sevenSinCoin)


# Genesis Boss 1 - 「創る、この世界を」（前編）
gen1Ev = "gen1Ev.png"
gen1Logo = "gen1Logo.png"
gen1Stage = "gen1Stage.png"
genCoin = "gen1Coin.png"
genesis1 = spQ(gen1Ev, "left", gen1Logo, gen1Stage, genCoin)

# Genesis Boss 2 - 「創る、この世界を」（後編）
gen2Ev = "gen2Ev.png"
gen2Logo = "gen2Logo.png"
gen2Stage = "gen2Stage.png"
genesis2 = spQ(gen2Ev, "left", gen2Logo, gen2Stage, genCoin)

# Genesis Boss 3 - 「恋と、色欲の偏差」（前編）
gen3Ev = "gen3Ev.png"
gen3Logo = "gen3Logo.png"
gen3Stage = "gen3Stage.png"
genesis3 = spQ(gen3Ev, "left", gen3Logo, gen3Stage, genCoin)

# Genesis Boss 4 - 「恋と、色欲の偏差」（後編）
gen4Ev = "gen4Ev.png"
gen4Logo = "gen3Logo.png"
gen4Stage = "gen3Stage.png"
genesis4 = spQ(gen4Ev, "left", gen4Logo, gen4Stage, genCoin)

#  -------------------------Define Function-------------------------
# Go to special event
def gotoSP(spQ):
	if not exists(spQ.stage, 0):
		sysMsg("Going to selected special event")
		if not exists(spQ.logo, 0):
			if not exists(spQ.event, 0):
				if exists(home, 0):
					click(home)
				if spQ.menuLoc == "up":
					clkObj(SP, None, True)
				if spQ.menuLoc == "left":
					clkObj(SPX, None, True)
			while not exists(spQ.event, double):
				click(questArrow)
			clkObj(spQ.event)
		if spQ.menuLoc == "up":
			clkObj(bossHard)
		if spQ.menuLoc == "left":
			clkObj(bossHardX)
		clkObj(spStart)
	else:
		sysMsg("Already in selected special event")


# After entering battle, toggle Auto if not On, and complete.
def spAction(reward):
	wait(btMenu, 30)
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
		clkObj(reward)
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
		clkObj(bossHard)
	#if n == "all":
	#	while not exists(noTicket)
		#	clkObj(spStart)
		#	teamSelect(team)
		#	clkObj(btStart)
		#	spAction(spQ.reward)
		#	i = i + 1
		#	sysMsg("Successfully executed " + str(i) + " time(s); killed boss " + str(c) + " time(s)")
		#	sleep(normal)	
	while i < n:
		clkObj(spStart)
		sleep(double)
		try:
			find(btStart)
			#teamSelect(team)
			clkObj(btStart)
			spAction(spQ.reward)
			i = i + 1
			sysMsg("Successfully executed " + str(i) + " time(s); killed boss " + str(c) + " time(s)")
		except FindFailed:
			sysMsg("Error: Cannot find btStart button. Not enough ticket?")
			i = n
	else:
		if n < 0:
			sysMsg("Error: n must be empty or positive")
		else:
			pass


def spDraw(n=1):
	sysMsg("Initializing SpecialEventDraw command")
	i = 0
	if exists(evDraw,0):
		clkObj(evDraw)
	if exists(evDrawX,0):
		clkObj(evDrawX)
	clkObj(evDraw10)
	if exists(empty, 0.5):
		clkObj(spOK)
		sleep(normal)
		clkObj(spOK)
		clkObj(evDraw10)
	if exists(noCoin, 0):
		clkObj(spOK)
		sysMsg("No more coins available")
	else:
		try:
			clkObj(drawing)
			i = i + 1
		except FindFailed:
			pass
		sysMsg("Successfully executed 1st time")
		if n == "all":
			while not exists(noCoin):
				clkObj(evDraw10)
				if exists(empty, 0.5):
					clkObj(spOK)
					sleep(normal)
					clkObj(spOK)
					clkObj(evDraw10)
				i = i + 1
				try:
					click(drawing)
				except FindFailed:
					pass
				sysMsg("Successfully executed " + str(i) + " times")
				if exists(noCoin):
					clkObj(spOK)
					sysMsg("No more coins available")
		else:
			while i < n:
				clkObj(evDraw10)
				if exists(empty, 0.5):
					clkObj(spOK)
					sleep(normal)
					clkObj(spOK)
					clkObj(evDraw10)
				if not exists(noCoin, 0):
					try:
						clkObj(drawing)
						i = i + 1
					except FindFailed:
						pass
					sysMsg("Successfully executed " + str(i) + " times")
				else:
					clkObj(spOK)
					sysMsg("No more coins available")
					i = n
			else:
				if n < 0:
					sysMsg("Error: n must be empty or positive")
				else:
					pass



#  -------------------------Command-------------------------
spDraw("all")
# spBoss(sevenSin, 1)
# spBoss(genesis4, 18)
# spBoss(movie2, 6)
# spBoss(fgg, 5)
# spBoss(drama, 8)