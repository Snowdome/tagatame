 # spEvent.py last updated 03/08/2020

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for special event
class spQ():
	def __init__(self, name, event, menuLoc, logo, stage, reward):
		self.name = name
		self.event = event
		self.menuLoc = menuLoc	# advance or genesis
		self.logo = logo
		self.stage = stage
		self.reward = reward


#  -------------------------Assets-------------------------
gen = "gen.png"
bbq = "bbq.png"
bbqQuest = "bbqQuest.png"
bbqNormal = "bbqNormal.png"
bbqHard = "bbqHard.png"
bbqEx = "bbqEx.png"
bbqModeSwitch = Pattern("mainMenu.png").targetOffset(-810,65)	# Location of mode button in respect to the menu button
bbqOK = "bbqOK.png"
bbqBack = "bbqBack.png"
stage1 = Pattern("mainMenu.png").targetOffset(-745,205)	# Location of stage 1 in respect to the menu button
stage2 = Pattern("mainMenu.png").targetOffset(-620,295)	# Location of stage 2 button in respect to the menu button
stage3 = Pattern("mainMenu.png").targetOffset(-490,205)	# Location of stage 3 button in respect to the menu button
stage4 = Pattern("mainMenu.png").targetOffset(-355,295)	# Location of stage 4 button in respect to the menu button
stage5 = Pattern("mainMenu.png").targetOffset(-230,205)	# Location of stage 5 button in respect to the menu button
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
movie1 = spQ("「劇場版 誰ガ為のアルケミスト」前編", "movie1Ev.png", "adv", "movie1Logo.png", "movie1Stage.png", "movie1Coin.png")

# Advance Boss Movie02 - 「劇場版 誰ガ為のアルケミスト」中編
movie2 = spQ("「劇場版 誰ガ為のアルケミスト」中編", "movie2Ev.png", "adv", "movie2Logo.png", "movie2Stage.png", "movie2Coin.png")

# Advane Boss Movie03 - 「劇場版 誰ガ為のアルケミスト」後編
movie3 = spQ("「劇場版 誰ガ為のアルケミスト」後編", "movie3Ev.png", "adv", "movie3Logo.png", "movie3Stage.png", "movie3Coin.png")

# Advance Boss 3Title - すなわち恋の雪景色
fgg = spQ("すなわち恋の雪景色", "fggEv.png", "adv", "fggLogo.png", "fggStage.png", "fggCoin.png")

# Advance Boss Butai - 誓いの刃、貫く魔槍
drama = spQ("誓いの刃、貫く魔槍", "dramaEv.png", "adv", "dramaLogo.png", "dramaStage.png", "dramaCoin.png")

# Advance Boss Novel - 姉弟とヒトリの剣士
# Missing

# Advnace Boss Templar - 七色琥珀のサンセリフ
as1 = spQ("七色琥珀のサンセリフ", "as1Ev.png", "adv", "as1Logo.png", "as1Stage.png", "asCoin.png")

# Advnace Boss Templar - うるさいよ五月雨
as2 = spQ("うるさいよ五月雨", "as2Ev.png", "adv", "as2Logo.png", "as2Stage.png", "asCoin.png")

# Advnace Boss Templar - 麒麟×靴底スタンドアロン
as3 = spQ("麒麟×靴底スタンドアロン", "as3Ev.png", "adv", "as3Logo.png", "as3Stage.png", "asCoin2.png")

# Advnace Boss Templar - 四辻夢幻によろしく
as4 = spQ("四辻夢幻によろしく", "as4Ev.png", "adv", "as4Logo.png", "as4Stage.png", "asCoin.png")

# Advance Boss Crossover - 夜明けに奏でるクレーデレ
sevenSin = spQ("夜明けに奏でるクレーデレ", "7sinEv.png", "adv", "7sinLogo.png", "7sinStage.png", "7sinCoin.png")

# Advance Boss Crossover - 捻じれ時空のスカベンジャー
slime = spQ("捻じれ時空のスカベンジャー", "slimeEv.png", "adv", "slimeLogo.png", "slimeStage.png", "slimeCoin.png")

# Advance Boss Crossover - 波打ち際モラトリアム
shield = spQ("波打ち際モラトリアム", "shieldEv.png", "adv", "shieldLogo.png", "shieldStage.png", "shieldCoin.png")


# Genesis Boss 1 - 「創る、この世界を」（前編）
gen1 = spQ("「創る、この世界を」（前編）", "gen1Ev.png", "gen", "gen1Logo.png", "gen1Stage.png", "genCoin.png")

# Genesis Boss 2 - 「創る、この世界を」（後編）
gen2 = spQ("創る、この世界を」（後編）", "gen2Ev.png", "gen", "gen2Logo.png", "gen2Stage.png", "genCoin.png")

# Genesis Boss 3 - 「恋と、色欲の偏差」（前編）
gen3 = spQ("「恋と、色欲の偏差」（前編）", "gen3Ev.png", "gen", "gen3Logo.png", "gen3Stage.png", "genCoin.png")

# Genesis Boss 4 - 「恋と、色欲の偏差」（後編）
gen4 = spQ("「恋と、色欲の偏差」（後編）", "gen4Ev.png", "gen", "gen3Logo.png", "gen3Stage.png", "genCoin.png")

# Genesis Boss 5 - 「それを怠惰と呼ぶのなら」（前編）
gen5 = spQ("「それを怠惰と呼ぶのなら」（前編）", "gen5Ev.png", "gen", "gen5Logo.png", "gen5Stage.png", "genCoin.png")

# Genesis Boss 6 - 「それを怠惰と呼ぶのなら」（後編）
gen6 = spQ("「それを怠惰と呼ぶのなら」（後編）", "gen6Ev.png", "gen", "gen6Logo.png", "gen6Stage.png", "genCoin.png")

# Genesis Boss 7 - 「その暴食をも呑み干して」（前編）
gen7 = spQ("「その暴食をも呑み干して」（前編）", "gen7Ev.png", "gen", "gen7Logo.png", "gen7Stage.png", "genCoin.png")

# Genesis Boss 8 - 「その暴食をも呑み干して」（後編）
gen8 = spQ("「その暴食をも呑み干して」（後編）", "gen8Ev.png", "gen", "gen8Logo.png", "gen8Stage.png", "genCoin.png")

# Genesis Boss 9 - 「嫉妬が胸を灼こうとも」（前編）
gen9 = spQ("「嫉妬が胸を灼こうとも」（前編）", "gen9Ev.png", "gen", "gen9Logo.png", "gen9Stage.png", "genCoin.png")

# Genesis Boss 10 - 「嫉妬が胸を灼こうとも」（前編）
gen10 = spQ("「嫉妬が胸を灼こうとも」（前編）", "gen10Ev.png", "gen", "gen10Logo.png", "gen10Stage.png", "genCoin.png")

#  -------------------------Define Function-------------------------
# Go to special event
def gotoSP(spQ, mode="boss"):
	if not exists(spQ.stage, 0):
		sysMsg("Going to selected special event")
		if not exists(spQ.logo, 0):
			if not exists(spQ.event, 0):
				if exists(home, 0):
					clkObj(mainMenu)
					clkObj(questLoc)
				else:
					clkObj(quest)
				if spQ.menuLoc == "gen":
					clkObj(story)
					clkObj(gen, 0, 1)
				if spQ.menuLoc == "adv":
					clkObj(event)
					clkObj(bbq, 0, 1)
				sleep(changePage)
			while not exists(spQ.event, double):
				clkObj(questArrow)
			clkObj(spQ.event)
		if mode == "boss":
			if spQ.menuLoc == "gen":
				clkObj(bossHard)
			if spQ.menuLoc == "adv":
				clkObj(bossHardX)
			clkObj(spStart)
		else:
			clkObj(bbqQuest, 0, bbqNormal)
			while not exists(mode):
				clkObj(bbqModeSwitch)
				sleep(1)
	else:
		sysMsg("Already in selected special event")


# After entering battle, toggle Auto if not On, and complete.
def spAction(reward):
	t = 0
	wait(btMenu, 30)
	if exists(toggleAuto, normal):
		click(toggleAuto)
		sysMsg("Toggled auto")
		sleep(short)
	else:
		sysMsg("Auto already on")
	while t != -1:
		if not exists(reward, 0):
			sysMsg("Still in battle. Waiting for 10 more sec. Total waiting time: " + str(t) + " sec.")
			t = t + 10
			sleep (10)
		else:
			sysMsg("Reward icon found.")
			t = -1

def spAction(stage, remark):
	clkObj(stage, remark=remark)
	clkObj(bbqOK)
	clkObj(btStart)
	apCheck(btStart)
	if exists(noQuota):
		clkObj(noQuotaOK)
		clkObj(bbqBack)
	else:
		btAction(loop=2)
	clkObj(bbqBack)
	sysMsg("***** Completed " + str(remark) + ".*****")

def spStory(spQ, mode=bbqHard):
	sysMsg("Initializing SpecialEventStory command - " + spQ.name + ".")
	gotoSP(spQ, mode)
	spAction(stage1, "Stage 1")
	spAction(stage2, "Stage 2")
	spAction(stage3, "Stage 3")
	spAction(stage4, "Stage 4")
	spAction(stage5, "Stage 5")
	sysMsg("***************Completed SpecialEventStory command - " + spQ.name + ".***************")
	
	

# Start battle - hard boss
def spBoss(spQ, n=1):
	sysMsg("Initializing SpecialEventBoss command")
	i = 0
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
			if exists(spStart):
				sysMsg("Quest failed")
			else:
				sysMsg("Quest completed")
				clkObj(reward)
				c = c + 1
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
#spDraw("all")
spStory(gen10, bbqHard)
spStory(gen9, bbqHard)
spStory(gen8, bbqHard)
spStory(gen7, bbqHard)
spStory(gen6, bbqHard)
spStory(gen5, bbqHard)
spStory(gen4, bbqHard)
spStory(gen3, bbqHard)
spStory(gen2, bbqHard)
spStory(gen1, bbqHard)