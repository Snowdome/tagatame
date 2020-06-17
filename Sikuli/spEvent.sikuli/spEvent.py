# spEvent.py last updated 14/06/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for special event
class spQ():
	def __init__(self, event, menuLoc, logo, stage, reward):
		self.event = event
		self.menuLoc = menuLoc	# advance or genesis
		self.logo = logo
		self.stage = stage
		self.reward = reward


#  -------------------------Assets-------------------------

bbq = "bbq.png"
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
# Advance Boss Movie01 - 「劇場版 誰ガ為のアルケミスト」前編
movie1 = spQ("movie1Ev.png", "adv", "movie1Logo.png", "movie1Stage.png", "movie1Coin.png")

# Advance Boss Movie02 - 「劇場版 誰ガ為のアルケミスト」中編
movie2 = spQ("movie2Ev.png", "adv", "movie2Logo.png", "movie2Stage.png", "movie2Coin.png")

# Advane Boss Movie03 - 「劇場版 誰ガ為のアルケミスト」後編
movie3 = spQ("movie3Ev.png", "adv", "movie3Logo.png", "movie3Stage.png", "movie3Coin.png")

# Advance Boss 3Title - すなわち恋の雪景色
fgg = spQ("fggEv.png", "adv", "fggLogo.png", "fggStage.png", "fggCoin.png")

# Advance Boss Butai - 誓いの刃、貫く魔槍
drama = spQ("dramaEv.png", "adv", "dramaLogo.png", "dramaStage.png", "dramaCoin.png")

# Advance Boss Novel - 姉弟とヒトリの剣士
# Missing

# Advnace Boss Templar - 七色琥珀のサンセリフ
as1 = spQ("as1Ev.png", "adv", "as1Logo.png", "as1Stage.png", "asCoin.png")

# Advnace Boss Templar - うるさいよ五月雨
as2 = spQ("as2Ev.png", "adv", "as2Logo.png", "as2Stage.png", "asCoin.png")

# Advnace Boss Templar - うるさいよ五月雨
as3 = spQ("as3Ev.png", "adv", "as3Logo.png", "as3Stage.png", "asCoin2.png")

# Advnace Boss Templar - 四辻夢幻によろしく
as4 = spQ("as4Ev.png", "adv", "as4Logo.png", "as4Stage.png", "asCoin.png")

# Advance Boss Crossover - 夜明けに奏でるクレーデレ
sevenSin = spQ("7sinEv.png", "adv", "7sinLogo.png", "7sinStage.png", "7sinCoin.png")

# Advance Boss Crossover - 捻じれ時空のスカベンジャー
slime = spQ("slimeEv.png", "adv", "slimeLogo.png", "slimeStage.png", "slimeCoin.png")

# Advance Boss Crossover - 波打ち際モラトリアム
shield = spQ("shieldEv.png", "adv", "shieldLogo.png", "shieldStage.png", "shieldCoin.png")


# Genesis Boss 1 - 「創る、この世界を」（前編）
gen1 = spQ("gen1Ev.png", "gen", "gen1Logo.png", "gen1Stage.png", "genCoin.png")

# Genesis Boss 2 - 「創る、この世界を」（後編）
gen2 = spQ("gen2Ev.png", "gen", "gen2Logo.png", "gen2Stage.png", "genCoin.png")

# Genesis Boss 3 - 「恋と、色欲の偏差」（前編）
gen3 = spQ("gen3Ev.png", "gen", "gen3Logo.png", "gen3Stage.png", "genCoin.png")

# Genesis Boss 4 - 「恋と、色欲の偏差」（後編）
gen4 = spQ("gen4Ev.png", "gen", "gen3Logo.png", "gen3Stage.png", "genCoin.png")

# Genesis Boss 5 - 「それを怠惰と呼ぶのなら」（前編）
gen5 = spQ("gen5Ev.png", "gen", "gen5Logo.png", "gen5Stage.png", "genCoin.png")

# Genesis Boss 6 - 「それを怠惰と呼ぶのなら」（後編） ハードボス
gen6 = spQ("gen6Ev.png", "gen", "gen6Logo.png", "gen6Stage.png", "genCoin.png")

#  -------------------------Define Function-------------------------
# Go to special event
def gotoSP(spQ):
	if not exists(spQ.stage, 0):
		sysMsg("Going to selected special event")
		if not exists(spQ.logo, 0):
			if not exists(spQ.event, 0):
				if exists(home, 0):
					clkObj(mainMenu)
				clkObj(questLoc)
				if spQ.menuLoc == "gen":
					clkObj(story)
					clkObj("1578161614894.png", 0, 1)
				if spQ.menuLoc == "adv":
					clkObj(event)
					clkObj(bbq, 0, 1)
				sleep(changePage)
			while not exists(spQ.event, double):
				clkObj(questArrow)
			clkObj(spQ.event)
		if spQ.menuLoc == "gen":
			clkObj(bossHard)
		if spQ.menuLoc == "adv":
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
		if not exists(bossHard):
			gotoSP(spQ)
		else:
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
			sysMsg("***************Successfully executed " + str(i) + " time(s); killed boss " + str(c) + " time(s)***************")
		except FindFailed:
			sysMsg("Error: Cannot find btStart button. Not enough ticket?")
			i = n
	else:
		if n < 0:
			sysMsg("Error: n must be empty or positive")
		else:
			sysMsg("Function end. Sleeping for " + str(changePage) + "sec.")
			sleep(changePage)
			clkObj(back)
			sleep(double)


def spDraw(n=1):
	sysMsg("Initializing SpecialEventDraw command")
	i = 0
	if exists(btStart, 0):
		clkObj(back)
		sleep(normal)
	if exists(spStart, 0):
		clkObj(back)
		sleep(changePage)
	if exists(evDraw, 0):
		clkObj(evDraw)
	if exists(evDrawX, 0):
		clkObj(evDrawX)
	clkObj(evDraw10, 0, 0, "Event Draw-10")
	if exists(empty, 0.5):
		clkObj(spOK)
		sleep(normal)
		clkObj(spOK)
		clkObj(evDraw10, 0, 0, "Event Draw-10")
	if exists(noCoin, 0):
		clkObj(spOK)
		sysMsg("No more coins available")
	else:
		try:
			#clkObj(drawing)
			i = i + 1
		except FindFailed:
			pass
		sysMsg("***************Successfully executed 1st time***************")
		if n == "all":
			while not exists(noCoin):
				clkObj(evDraw10, 0, 0, "Event Draw-10")
				if exists(empty, 0.5):
					clkObj(spOK)
					sleep(normal)
					clkObj(spOK)
					clkObj(evDraw10, 0, 0, "Event Draw-10")
				try:
					#click(drawing)
					i = i + 1
				except FindFailed:
					pass
				sysMsg("***************Successfully executed " + str(i) + " times***************")
				if exists(noCoin):
					clkObj(spOK)
					sysMsg("No more coins available")
		else:
			while i < n:
				clkObj(evDraw10, 0, 0, "Event Draw-10")
				if exists(empty, 0.5):
					clkObj(spOK)
					sleep(normal)
					clkObj(spOK)
					clkObj(evDraw10, 0, 0, "Event Draw-10x")
				if not exists(noCoin, 0):
					try:
						#clkObj(drawing)
						i = i + 1
					except FindFailed:
						pass
					sysMsg("***************Successfully executed " + str(i) + " times***************")
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
#spBoss(as2, 551/40)
spDraw("all")
#spDraw("all")