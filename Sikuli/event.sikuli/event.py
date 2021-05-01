# event.py last updated 25/04/2021

#  -------------------------Import Modules and Classes-------------------------
import tagatame
reload(tagatame)
from tagatame import *


# Define class for special event
class evQ():
	def __init__(self, event, stat, stage, title):
		self.event = event
		self.stat = stat	# Current or Archive or Key or Daily event
		self.stage = stage
		self.title = title


#  -------------------------Assets-------------------------
evArchive = "evArchive.png"
evAOT = "evAOT.png"
evPOK = "evPOK.png"
access = "access.png"

#  -------------------------Variables-------------------------
# Side Stories
arena = evQ(Pattern("1609670830838.png").targetOffset(-150,0), "Archive", "1609669649653.png", "1609669662183.png") #幻影兵対抗大運動会
bloodWolf = evQ(Pattern("1609671341370.png").targetOffset(-150,0), "Archive", "1609670441919.png", "1609670449786.png") #血狼と呼ばれても
hisham = evQ(Pattern("1609670840284.png").targetOffset(-150,0), "Archive", "1609669733828.png", "1609669744199.png") #『ヒシャーム』のクラスチェンジクエスト
merchant = evQ(Pattern("merchantEv.png").targetOffset(435,40), "Key", "merchantStage.png", "merchantTitle.png") #砂漠の商人
pipa = evQ(Pattern("pipaEv.png").targetOffset(425,35), "Key", "pipaStage.png", "pipaTitle.png") #出逢いと運命とピパの音と
scarlet = evQ(Pattern("1609670533453.png").targetOffset(-150,0), "Archive", "1609668451682.png", "1609668460440.png") #託された緋炎、約束の先へ
shayna = evQ(Pattern("1609671080848.png").targetOffset(-150,0), "Archive", "1609669161989.png", "1609669169921.png") #その師匠、稲妻につき
starlight = evQ(Pattern("starlightEv.png").targetOffset(425,35), "Key", "starlightStage.png", "starlightTitle.png") #絆は星が燃えるより永く
wrath = evQ(Pattern("1609670558629.png").targetOffset(-150,0), "Archive", "1609668686706.png", "1609668694461.png") #この薄汚れた世界に生きて
yudit = evQ(Pattern("1609670586655.png").targetOffset(-150,0), "Archive", "yuditStage.png", "yuditTile.png") #繋ぐ明日へのメカニカル
yura = evQ("1619317952458.png", "Current", "1619317969325.png", "1619317979844.png") #垣根無く、未来へ

# Seasons
easter2020 = evQ(Pattern("1609671093657.png").targetOffset(-150,0), "Archive", "easterStage.png", "easterTitle.png") #魔法仕掛けのColorful Egg
halloween2016 = evQ(Pattern("1609671318146.png").targetOffset(-150,0), "Archive", "1609670347956.png", "1609670357381.png") #ハロウィン★シュガーラッシュ！
halloween2017 = evQ(Pattern("1609671194909.png").targetOffset(-150,0), "Archive", "halloween2018Stage.png", "halloween2018Title.png") #チューチュー★ハロウィン!!
halloween2018 = evQ(Pattern("1609671151534.png").targetOffset(-150,0), "Archive", "1609669516283.png", "1609669530781.png") #Trick or Flower!!
halloween2019 = evQ(Pattern("1609671065022.png").targetOffset(-150,0), "Archive", "1609672485927.png", "1589093890927.png") #ハロウィン狂騒曲～紅と闇の輪舞～
halloween2020 = evQ(Pattern("1609670493385.png").targetOffset(-150,0), "Archive", "1609668382721.png", "1609668391854.png") #Sunshine・Halloween
harvestMoon = evQ(Pattern("1609671033690.png").targetOffset(-150,0), "Archive", "harvestMoonStage.png", "harvestMoonTitle.png") #Harvest Moonの約束
summer2016= evQ(Pattern("1609671328474.png").targetOffset(-150,0), "Archive", "1609670401194.png", "1609670408005.png") #荒ぶる海の漢
summer2017 = evQ(Pattern("1609671267275.png").targetOffset(-150,0), "Archive", "1609670133925.png", "1609670142678.png") #荒ぶる海の漢 猛装伝
summer2018 = evQ(Pattern("1609671206561.png").targetOffset(-150,0), "Archive", "1609669855428.png", "1609669862645.png") #ワンダフル☆SUMMER
summer2019 = evQ(Pattern("1609671046816.png").targetOffset(-150,0), "Archive", "1609674743917.png", "pirateTitle.png") #机上の空論、八本足
summer2020 = evQ(Pattern("1609670855581.png").targetOffset(-150,0), "Archive", "1609674321319.png", "summer2020Title.png") #渚のトラブルシューティング
vDay2017 = evQ(Pattern("1609671293056.png").targetOffset(-150,0), "Archive", "1609670233082.png", "1609670243721.png") #チョコレート・トイボックス
vDay2018 = evQ(Pattern("1609671243473.png").targetOffset(-150,0), "Archive", "1609670006920.png", "1609670014794.png") #ちょこれいと☆まじっく
vDay2019 = evQ(Pattern("1609671126746.png").targetOffset(-150,0), "Archive", "vDay2018Stage.png", "vDayy2018Title.png") #Spicy Chocolate Battle
vDay2020 = evQ(Pattern("1609670991118.png").targetOffset(-150,0), "Archive", "1609674297891.png", "vDayTitle.png") #チョコレート・ハートミックス
vDay2021 = evQ("1614382524492.png", "Current", "1614382536722.png", "1614382546378.png") #Chocolate tradeにご用心
wedding2017 = evQ(Pattern("1609671282052.png").targetOffset(-150,0), "Archive", "1609670186754.png", "1609670193790.png") #Marriage-Go-Round
wedding2018 = evQ(Pattern("1609671224428.png").targetOffset(-150,0), "Archive", "1609669924925.png", "1609669934161.png") #Happy Happy Crazy Wedding!
wedding2020 = evQ(Pattern("1609670870490.png").targetOffset(-150,0), "Archive", "1609668965152.png", "1609668972044.png") #Wedding Knifeに祝福を
wVday2019 = evQ(Pattern("1609671112346.png").targetOffset(-150,0), "Archive", "1609669307116.png", "1609669398765.png") #ホワイトデー・コンプレックス
wVday2020 = evQ(Pattern("1609670948562.png").targetOffset(-150,0), "Archive", "1609673255716.png", "whiteVdayTitle.png") #おもてなしは愛をこめて
wVday2020b= evQ(Pattern("1609670519685.png").targetOffset(-150,0), "Archive", "1609668322128.png", "1609668330328.png") #永遠を紡ぐラブレター
xmas2016 = evQ(Pattern("1609671306222.png").targetOffset(-150,0), "Archive", "1609670290531.png", "1609670300419.png") #クリスマス・タイム・イン・バベル
xmas2017 = evQ(Pattern("1609671252645.png").targetOffset(-150,0), "Archive", "1609670062640.png", "1609670069282.png") #A Snow White Christmas
xmas2018 = evQ(Pattern("1609671139719.png").targetOffset(-150,0), "Archive", "xmas2018Stage.png", "xmas2018Title.png") #雪だるまから愛をこめて
xmas2019 = evQ(Pattern("1609671003855.png").targetOffset(-150,0), "Archive", "xmasStage.png", "xmasTitle.png") #よいこのためのクリスマス計画
xmas2020 = evQ(Pattern("1609670507657.png").targetOffset(-150,0), "Current", "1609668244324.png", "1609668256320.png") #Wish your Happy Xmas

# Collab
AOT = evQ("AOTEvHard.png", "AOT", "AOTStage.png", "aotTitle.png") #紡ぐ彼方のメカニカル
AOT2 = evQ("AOTEvHell.png", "AOT", "AOT2Stage.png", "aot2Title.png") #紡ぐ彼方のメカニカル
POKL1 = evQ("1619317644373.png", "POK", "1619317689465.png", "1619317715360.png")
POK10 = evQ("1619317604855.png", "POK", "1604806963152.png", "1604806975054.png")
POK12 = evQ("1619317604855.png", "POK", "POK12Stage.png", "POK12Title.png")
shieldBallon = evQ("1589098452707.png", "Current", "shieldBallonStage.png", "shieldBallonTitle.png") #オレンジバルーン大発生

# Misc
wrathArmorF = evQ(Pattern("wrathArmorFEv.png").targetOffset(-150,0), "Archive", "wrathArmorFStage.png", "wrathArmorFTitle.png")
statue1 = evQ("statue1.png", "Daily", "statueStage.png", Pattern("statue1Title.png").exact())
statue2 = evQ("statue2.png", "Daily", "statueStage.png", Pattern("statue2Title.png").exact())
statue3 = evQ("statue3.png", "Daily", "statueStage.png", Pattern("statue3Title.png").exact())
statue4 = evQ("statue4.png", "Daily", "statueStage.png", Pattern("statue4Title.png").exact())
statue5 = evQ("statue5.png", "Daily", "statueStage.png", Pattern("statue5Title.png").exact())
statue6 = evQ("statue6.png", "Daily", "statueStage.png", Pattern("statue6Title.png").exact())


def gotoEv(evQ):
	if not exists(evQ.title, 0):
		sysMsg("Going to selected event")
		if not exists(evQ.stage, 0):
			if not exists(evQ.event, 0):
				if exists(home, 0):
					clkObj(mainMenu)
					clkObj(questLoc, 0, event, remark="questLoc")
				else:
					clkObj(quest)
				clkObj(event, 0, daily)
				if evQ.stat == "Daily":
					clkObj(daily, 0, eventTitle)
					sleep(15)
					while not exists(evQ.event, double):
						clkObj(questArrow)
						sysMsg("Turning page: daily quest")
				else:
					if evQ.stat == "Key":
						clkObj(archive, 0, access)
						while not exists(evQ.event, double):
							clkObj(archivePageDown)
							sysMsg("Turning page: event archives")
					else:
						clkObj(eventQ, 0, eventTitle)
						sleep(15)
						if evQ.stat == "Archive":
							while not exists(evArchive, double):
								clkObj(questArrow)
								sysMsg("Turning page: main quest")
							clkObj(evArchive)
						if evQ.stat == "AOT":
							while not exists(evAOT, double):
								clkObj(questArrow)
								sysMsg("Turning page: main quest")
							clkObj(evAOT)
						if evQ.stat == "POK":
							while not exists(evPOK, double):
								clkObj(questArrow)
								sysMsg("Turning page: main quest")
							clkObj(evPOK)
						while not exists(evQ.event, double):
							clkObj(questArrow, remark="Quest Arrow")
							if evQ.stat == "Current":
								sysMsg("Turning page: main quest")
							if evQ.stat == "Archive":
								sysMsg("Turning page: archive quest")
			clkObj(evQ.event)
		clkObj(evQ.stage, 0, evQ.title)
	else:
		sysMsg("Already in selected event")

def evAR(evQ, n=10):
	i = 0
	if exists(arMenu):
		sysMsg("Ongoing auto repeat found. Waiting for completion.")
		arCheck()
		sleep(10)
		i = 1 + 1
	else:
		gotoEv(evQ)
		enableAR()
		waitObj(settings, 30)
		arCheck(loop=n)

#  -------------------------Command-------------------------
#arCheck(loop=10)
#evAR(vDay, 30)
#evAR(vDay2021, 5)
#evAR(yura, 10)
evAR(statue6, 30)