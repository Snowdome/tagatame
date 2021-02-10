   # spEvent.py last updated 24/12/2020

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
genQuest = "quest.png"
bbqQp = "bbqQp.png"
bbqNormal = "bbqNormal.png"
bbqHard = "bbqHard.png"
bbqEx = "bbqEx.png"
bbqModeSwitch = Pattern("mainMenu.png").targetOffset(-810,65)	# Location of mode button in respect to the menu button
bbqOK = "bbqOK.png"
bbqCancel = "bbqCancel.png"
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
evDrawBtn1 = "evDrawBtn1.png"
evDrawBtn2 = "evDrawBtn2.png"
evDrawMax = "evDrawMax.png"
evDrawConfirm = "evDrawConfirm.png"
evDrawSkip = "evDrawSkip.png"
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
novel = spQ("姉弟とヒトリの剣士", "novelEv.png", "adv", "novelLogo.png", "1609668054847.png", "novelCoin.png")

# Advnace Boss Templar - 七色琥珀のサンセリフ
as1 = spQ("AS1 七色琥珀のサンセリフ", "as1Ev.png", "adv", "as1Logo.png", "1609668024358.png", "asCoin.png")

# Advnace Boss Templar - うるさいよ五月雨
as2 = spQ("AS2 うるさいよ五月雨", "as2Ev.png", "adv", "as2Logo.png", "1609667982665.png", "asCoin.png")

# Advnace Boss Templar - 麒麟×靴底スタンドアロン
as3 = spQ("AS3 麒麟×靴底スタンドアロン", "as3Ev.png", "adv", "as3Logo.png", "1609667881695.png", "asCoin2.png")

# Advnace Boss Templar - 四辻夢幻によろしく
as4 = spQ("AS4 四辻夢幻によろしく", "as4Ev.png", "adv", "as4Logo.png", "1609667949494.png", "asCoin.png")

# Advnace Boss Templar - ズバリおのれの十紋葬
as5 = spQ("AS5 ズバリおのれの十紋葬", "as5Ev.png", "adv", "as5Logo.png", "1609667911058.png", "asCoin.png")

# Advnace Boss Templar - 冥弩メメント＆ロイド
as6 = spQ("AS6 冥弩メメント＆ロイド", "as6Ev.png", "adv", "as6Logo.png", "as6Stage.png", "asCoin.png")

# Advance Boss Collab - 夜明けに奏でるクレーデレ
sevenSin = spQ("夜明けに奏でるクレーデレ", "7sinEv.png", "adv", "7sinLogo.png", "7sinStage.png", "7sinCoin.png")

# Advance Boss Collab - 捻じれ時空のスカベンジャー
slime = spQ("捻じれ時空のスカベンジャー", "slimeEv.png", "adv", "slimeLogo.png", "slimeStage.png", "slimeCoin.png")

# Advance Boss Collab - 波打ち際モラトリアム
shield = spQ("波打ち際モラトリアム", "shieldEv.png", "adv", "shieldLogo.png", "shieldStage.png", "shieldCoin.png")

# Advance Boss Collab - Re:ゼロから始める異世界生活
reZero = spQ("Re:ゼロから始める異世界生活", "reZeroEv.png", "adv", "reZeroLogo.png", "reZeroStage.png", "reZeroCoin.png")

# Advance Boss Collab - 拳に宿りしは誰ガ為の
kof = spQ("拳に宿りしは誰ガ為の", "1609675651248.png" , "adv", "1609675625057.png", "1609675692125.png", "1609675672525.png")

# Advance Boss - Wild Card Hero
WCH = spQ("Wild Card Hero", "1602106517367.png", "adv", "1602106537649.png", "1609668093389.png", "1602106560384.png")

# Genesis 1A - 「創る、この世界を」（前編）
gen1a = spQ("1A 「創る、この世界を」（前編）", "gen1aEv.png", "gen", "gen1aLogo.png", "gen1aStage.png", "genCoin.png")

# Genesis 1B - 「創る、この世界を」（後編）
gen1b = spQ("1B 創る、この世界を」（後編）", "gen1bEv.png", "gen", "gen1bLogo.png", "gen1bStage.png", "genCoin.png")

# Genesis 2A - 「恋と、色欲の偏差」（前編）
gen2a = spQ("2A 「恋と、色欲の偏差」（前編）", "gen2aEv.png", "gen", "gen2aLogo.png", "gen2aStage.png", "genCoin.png")

# Genesis 2B - 「恋と、色欲の偏差」（後編）
gen2b = spQ("2B 「恋と、色欲の偏差」（後編）", "gen2bEv.png", "gen", "gen2bLogo.png", "gen2bStage.png", "genCoin.png")

# Genesis 3A - 「それを怠惰と呼ぶのなら」（前編）
gen3a = spQ("3A 「それを怠惰と呼ぶのなら」（前編）", "gen3aEv.png", "gen", "gen3aLogo.png", "gen3aStage.png", "genCoin.png")

# Genesis 3B - 「それを怠惰と呼ぶのなら」（後編）
gen3b = spQ("3B 「それを怠惰と呼ぶのなら」（後編）", "gen3bEv.png", "gen", "gen3bLogo.png", "gen3bStage.png", "genCoin.png")

# Genesis 4A - 「その暴食をも呑み干して」（前編）
gen4a = spQ("4A 「その暴食をも呑み干して」（前編）", "gen4aEv.png", "gen", "gen4aLogo.png", "gen4aStage.png", "genCoin.png")

# Genesis 4B - 「その暴食をも呑み干して」（後編）
gen4b = spQ("4B 「その暴食をも呑み干して」（後編）", "gen4bEv.png", "gen", "gen4bLogo.png", "gen4bStage.png", "genCoin.png")

# Genesis 5A - 「嫉妬が胸を灼こうとも」（前編）
gen5a = spQ("5A 「嫉妬が胸を灼こうとも」（前編）", "gen5aEv.png", "gen", "gen5aLogo.png", "gen5aStage.png", "genCoin.png")

# Genesis 5B - 「嫉妬が胸を灼こうとも」（後編）
gen5b = spQ("5B 「嫉妬が胸を灼こうとも」（後編）", "gen5bEv.png", "gen", "gen5bLogo.png", "gen5bStage.png", "genCoin.png")

# Gensos 6A - 「この憤怒こそ我が正義」（前編）
gen6a = spQ("6A 「この憤怒こそ我が正義」（前編）", "gen6aEv.png", "gen", "gen6aLogo.png", "gen6aStage.png", "genCoin.png")

# Gensos 6B - 「この憤怒こそ我が正義」（後編）
gen6b = spQ("6B 「この憤怒こそ我が正義」（後編）", "gen6bEv.png", "gen", "gen6bLogo.png", "gen6bStage.png", "genCoin.png")

# Gensos 7A - 「「強欲なるは我が心」（前編）
gen7a = spQ("7A 「強欲なるは我が心」（前編）", "1612221594340.png", "gen", "1612221616635.png", "1612221642262.png", "genCoin.png")

drop = Region(246,368,476,88)
ryui = "ryui.png"
nero1hit = Pattern("nero1hit.png").targetOffset(167,0)
WCH2 = Pattern("WCH2.png").targetOffset(165,0)
WCH3 = Pattern("WCH3.png").targetOffset(165,0)

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
					clkObj(quest, remark="Quest Loc")
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
		elif mode == "draw":
			sleep(3)
			if exists(evDraw, 0):
				clkObj(evDraw)
			if exists(evDrawX, 0):
				clkObj(evDrawX)
		else:
			if spQ.menuLoc == "gen":
				clkObj(genQuest, 0, bbqQp)
			if spQ.menuLoc == "adv":
				clkObj(bbqQuest, 0, bbqQp)
			sleep(2)
			while not exists(mode):
				clkObj(bbqModeSwitch)
				sleep(1)
	else:
		sysMsg("Already in selected special event (map screen)")
		if mode == bbqHard or mode ==bbqEx:
			while not exists(mode):
				clkObj(bbqModeSwitch)
				sleep(1)
			
				


# After entering battle, toggle Auto if not On, and complete.
def spBossAction(reward):
	t = 0
	waitObj(btMenu, 30)
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

def spAction(stage, mode, menuLoc, remark):
	errMsg = "Struck in" + str(remark) + " (post battle)."
	clkObj(stage, remark=remark)
	clkObj(bbqOK)
	if mode == bbqHard:
		if enableAR() == 0:
			clkObj(bbqBack)
		else:
			waitObj(autoRepeat, 30)
			arCheck(loop="return")
			waitObj(mode, 30)
	if mode == bbqEx:
		clkObj(btStart)
		apCheck(btStart)
		if exists(noQuota):
			clkObj(noQuotaOK)
			sysMsg("No remaining quota today. Returning to stage selection page.")
			clkObj(bbqBack)
		else:
			btAction(loop=0)
			waitObj(mode, 30)
	clkObj(bbqBack)
	waitObj(mode, 30, errMsg=errMsg)
	sysMsg("***** Completed " + str(remark) + ".*****")

def spStory(spQ, mode=bbqHard):
	sysMsg("Initializing SpecialEventStory command - " + spQ.name + ".")
	menuLoc = spQ.menuLoc
	gotoSP(spQ, mode)
	waitObj(mode, 15)
	remark = spQ.name + " Stage 1"
	spAction(stage1, mode, menuLoc, remark)
	remark = spQ.name + " Stage 2"
	spAction(stage2, mode, menuLoc, remark)
	remark = spQ.name + " Stage 3"
	spAction(stage3, mode, menuLoc, remark)
	remark = spQ.name + " Stage 4"
	spAction(stage4, mode, menuLoc, remark)
	remark = spQ.name + " Stage 5"
	spAction(stage5, mode, menuLoc, remark)
	sysMsg("***************Completed SpecialEventStory command - " + spQ.name + " (" + str(mode) + ")***************")
	
	

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
		#	spBossAction(spQ.reward)
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
			spBossAction(spQ.reward)
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


def spDraw(n=1000, spQ=0):
	if spQ != 0:
		sysMsg("Initializing SpecialEventDraw command - " + spQ.name)
	else:
		sysMsg("Initializing SpecialEventDraw command")
	i = 0
	if spQ != 0:
		gotoSP(spQ, mode="draw")
		sleep(2)
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
	clkObj(evDrawBtn2)
	sleep(1)
	if exists(noCoin, 0):
		clkObj(spOK)
		sysMsg("**********No more coins available**********")
		clkObj(bbqBack)
		clkObj(home)
		sleep(10)
		i = n
	else:
		if exists(empty, 0):
			clkObj(spOK)
			sleep(normal)
			clkObj(spOK)
			clkObj(evDrawBtn1)
			clkObj(evDrawMax)
		clkObj(evDrawConfirm)
		waitObj(evDrawSkip, 10, ff="skip")
		clkObj(evDrawSkip, ff="skip")
		i = i + 1
	while i < n:
		clkObj(evDrawBtn1)
		sleep(1)
		if exists(noCoin, 0):
			clkObj(spOK)
			sysMsg("**********No more coins available**********")
			clkObj(bbqCancel)
			clkObj(bbqBack)
			clkObj(home)
			sleep(10)
			i = n
		else:
			if exists(empty, 0):
				clkObj(spOK)
				sleep(normal)
				clkObj(spOK)
				clkObj(evDrawBtn1)
			clkObj(evDrawMax)
			clkObj(evDrawConfirm)
			waitObj(evDrawSkip, 10, ff="skip")
			clkObj(evDrawSkip, ff="skip")
			i = i + 1
		

def shard(unit, script, loop=2, m=0):
	i = 0
	while loop > -1:
		clkObj(bbqOK)
		clkObj(btStart)
		apCheck(btStart)
		if exists(noQuota):
			clkObj(noQuotaOK)
			sysMsg("No remaining quota today. Returning to stage selection page.")
			clkObj(bbqBack)
			loop = -1
		else:
			waitObj(btMenu, 30)
			i = i + 1
			sysMsg("*************** Total attempt: " + str (i) + " time(s) ***************")
			clkObj(script)
			waitObj(quitQuest, 60)
			capture(drop, "C:\Users\kklau\Desktop\capture", str(i))
			if not drop.exists(unit, 0):
				sysMsg("Unit shard not found, restarting.")
				clkObj(quitQuest)
				clkObj(confirm)
				waitObj(bbqOK, 30)
			else:
				loop = loop - 1
				sysMsg("Unit shard found.")
				clkObj(escMenu)
				clkObj(toggleAuto)
				t = 0
				while t != -1:
					if not exists(questMission, 0):
						sysMsg("Still in battle. Waiting for 1 more sec. Total waiting time: " + str(t) + " sec.")
						t = t + 1
						sleep(1)
					else:
						sysMsg("Quest completed.")
						clkObj(questMission, loop=1)
						t = -1
						i = i + 1
				click(reFocus)
				merchantCheck(m)
				if merchantCheck() == 1:
					m = 1
				clkObj(btEnd)
	return m

def shard_ryui():
	gotoSP(WCH, bbqHard)
	waitObj(bbqHard, 15)
	#remark = WCH.name + " Stage 1"
	#clkObj(stage1)
	#shard(ryui, nero1hit)
	#clkObj(bbqBack)
	remark = WCH.name + " Stage 2"
	#sleep(5)
	clkObj(stage2)
	shard(ryui, WCH2)
	clkObj(bbqBack)
	remark = WCH.name + " Stage 3"
	sleep(5)
	clkObj(stage3)
	shard(ryui, WCH3)
	clkObj(bbqBack)

def spStoryGen():
	# New story
	spStory(gen6b, bbqHard)
	spStory(gen6b, bbqEx)
	# Gem mining
	spStory(gen4b, bbqHard)
	spStory(gen4b, bbqEx)
	spStory(gen4a, bbqHard)
	spStory(gen4a, bbqEx)
	spStory(gen3b, bbqHard)
	spStory(gen3a, bbqHard)
	spStory(gen2b, bbqHard)
	spStory(gen2a, bbqHard)
	spStory(gen1b, bbqHard)
	spStory(gen1a, bbqHard)
	# No gem
	#spStory(gen6a, bbqHard)
	#spStory(gen6a, bbqEx)
	#spStory(gen5b, bbqHard)
	#spStory(gen5b, bbqEx)
	#spStory(gen5a, bbqHard)
	#spStory(gen5a, bbqEx)

def spStoryAs():
	# New story
	spStory(as6, bbqHard)
	spStory(as6, bbqEx)
	spStory(kof, bbqHard)
	spStory(kof, bbqEx)
	# Gem Mining
	spStory(as3, bbqHard)
	spStory(as3, bbqEx)
	spStory(as2, bbqHard)
	spStory(as1, bbqHard)
	# No gem
	#spStory(as5, bbqHard)
	#spStory(as5, bbqEx)
	#spStory(as4, bbqHard)
	#spStory(as4, bbqEx)

def mine(mode="gen"):
	if mode == "gen":
		spStory(gen7a, bbqEx)
		spStory(gen7a, bbqHard)
		spStory(gen4b, bbqEx)
		spStory(gen4a, bbqEx)
		spStory(gen4b, bbqHard)
		spStory(gen4a, bbqHard)
		spStory(gen3b, bbqHard)
		spStory(gen3a, bbqHard)
		spStory(gen2b, bbqHard)
		spStory(gen2a, bbqHard)
		spStory(gen1b, bbqHard)
		spStory(gen1a, bbqHard)
	if mode == "as":
		spStory(as3, bbqHard)
		spStory(as3, bbqEx)
		spStory(as2, bbqHard)
		spStory(as1, bbqHard)

def spDrawMine():
	spDraw(spQ=gen1a)
	spDraw(spQ=gen1b)
	spDraw(spQ=gen2a)
	spDraw(spQ=gen2b)
	spDraw(spQ=gen3a)
	spDraw(spQ=gen3b)
	spDraw(spQ=gen4a)
	spDraw(spQ=gen4b)

#  -------------------------Command-------------------------
#spBoss(as2, 551/40)
#spDrawMine()
spStory(as3, bbqHard)
spStory(as3, bbqEx)
mine("gen")
#arCheck(loop=10)