# pokPlugin.py last updated 27/10/2019

#  -------------------------Assets-------------------------
# Draw
pok_ticket = Pattern("pok_ticket.png").targetOffset(0,125)
pok_drawOnce = Pattern("pok_gachuHeader.png").targetOffset(-95,230)
pok_drawMax = Pattern("pok_gachuHeader.png").targetOffset(85,230)
pok_noMulti = Pattern("pok_noMulti.png").exact()
pok_dollMax = "pok_dollMax.png"
pok_noTicket = "pok_noTicket.png"
pok_skip = "pok_skip.png"
pok_pageNext = "pok_pageNext.png"
pok_pageBack = "pok_pageBack.png"

# Hime enchancement
pok_himeEn = Pattern("pok_himeEn.png").targetOffset(0,270)
pok_dollWhite = "pok_dollWhite.png"
pok_dollBlack = "pok_dollBlack.png"
pok_dollBrown = "pok_dollBrown.png"
pok_dollPurple = "pok_dollPurple.png"
pok_OK = "pok_OK.png"
pok_confirm = "pok_confirm.png"
pok_enStart = "pok_enStart.png"

# Gear forge
pok_selectGear = Pattern("pok_selectGear.png").targetOffset(-45,70)
pok_gearForge = Pattern("pok_gearForge.png").targetOffset(-10,315)
pok_selectOre = Pattern("pok_selectOre.png").targetOffset(-35,70)

pok_forgeStart = "pok_forgeStart.png"
pok_yes = "pok_yes.png"

# Battle
pok_stageMission = "pok_stageMission.png"
pok_affinity = Pattern("pok_affinity.png").similar(0.80)
pok_btResult = Pattern("pok_btResult.png").similar(0.90)
pok_loot = "pok_loot.png"
pok_pt = Pattern("pok_pt.png").targetOffset(110,575)
pok_accPt = "pok_accPt.png"
pok_ptAch = "pok_ptAch.png"
pok_btAgain = "pok_btAgain.png"
pok_btEndNext = "pok_btEndNext.png"
pok_btAP = "pok_btAP.png"
pok_btStart = "pok_btStart.png"

pok_keyUnlock = Pattern("pok_keyUnlock.png").similar(0.80)
pok_keyLv3 = "pok_keyLv3.png"
pok_keyStg = Pattern("pok_keyStg.png").targetOffset(130,415)

pok_egg = Pattern("pok_egg.png").similar(0.90)
pok_stats = "pok_stats.png" 
pok_train = "pok_train.png"
pok_himeRe = "pok_himeRe.png"
pok_menuBack = "pok_menuBack.png"
pok_reConfirm = "pok_reConfirm.png"

pok_unit1 = Pattern("pok_unit1.png").targetOffset(-215,-155)	#Offset for 1st unit slot
pok_gear1 = Pattern("pok_gear1.png").targetOffset(-30,60)	#Offset for 1st gear slot


#  -------------------------Define Function-------------------------
# Enhance hime with chosen doll
def enhance(doll, n=1):
	sysMsg("Initializing Enhance command")
	i = 0
	while i < n:
		clkObj(pok_himeEn)
		clkObj(pok_doll)
		clkObj(pok_OK)
		clkObj(pok_confirm)
		clkObj(pok_enStart)
		clkObj(pok_yes)
		while not exists(himeEn):
			click(atMouse())
			sleep(short)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Forge first gear with first ore
def forge(n=1):
	sysMsg("Initializing Forge command")
	i = 0
	while i < n:
		clkObj(pok_gearForge)
		clkObj(pok_selectOre)
		clkObj(pok_confirm)
		clkObj(pok_forgeStart)
		clkObj(pok_yes)
		sleep(double)
		click(atMouse())
		sleep(double)
		click(atMouse())
		#while not exists(pageBack):
		#	click(atMouse())
		#	sleep(short)
		clkObj(pok_pageBack)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Draw dolls
def drawDoll(n=1):
	sysMsg("Initializing DrawDoll command")
	i = 0
	while i < n:
		clkObj(pok_dollMax)
		clkObj(pok_skip)
		clkObj(pok_pageNext)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Draw ticket
def drawTicket(n=1):
	sysMsg("Initializing DrawTicket command")
	i = 0
	while i < n:
		clkObj(pok_ticket)
		if not exists(noMulti, short):
			clkObj(pok_drawMax)
			clkObj(pok_skip)
			clkObj(pok_pageNext)
			sleep(double)
		else:
			clkObj(pok_drawOnce)
			clkObj(pok_skip)
			clkObj(pok_pageBack)
			sleep(double)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Start battle for normal quest
def btAction(n=1):
	sysMsg("Initializing BattleAction command")
	i = 0
	while i < n:
		clkObj(pok_btStart)
		wait(pok_btResult, FOREVER)
		sleep(normal)
		while exists(pok_affinity):
			click(pok_affinity)
			sleep(double)
		clkObj(pok_btResult, normal, True, remark = "btResult")
		clkObj(pok_loot, normal, True)
		clkObj(pok_btAgain)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n < 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)

# Start battle for point quest
def btPtQuest(n=1):
	sysMsg("Initializing BattlePointQuest command")
	i = 0
	while i < n:
		clkObj(pok_btStart)
		wait(pok_btResult, FOREVER)
		while exists(pok_affinity):
			click(pok_affinity)
			sleep(double)
		while exists(pok_btResult):
			clkObj(pok_btResult, loading, remark = "btResult")
		clkObj(pok_loot, changePage)
		clkObj(pok_pt, changePage)
		clkObj(pok_accPt, double)
		while not exists(pok_btAgain):
			clkObj(pok_ptAch, double)
			sleep(double)
		clkObj(pok_btAgain)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
	else:
		if n <= 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)


# Start battle for unit quest
def btUnitQuest(n=1):
	sysMsg("Initializing UnitQuest command")
	i = 0
	while i < n:
		if exists(pok_btAgain, normal):
			clkObj(pok_btAgain)
		clkObj(pok_btStart)
		wait(pok_btResult, FOREVER)
		clkObj(pok_btResult, loading, remark = "btResult")
		while not exists(pok_pageNext):
			click(atMouse())
			sleep(normal)
		clkObj(pok_pageNext, changePage)
		while not exists(pok_btAgain):
			click(atMouse())
			sleep(double)
		clkObj(pok_btAgain)
		i = i + 1
		sysMsg("***************Successfully executed " + str(i) + " time(s)**************")
		sleep(normal)
	else:
		if n <= 0:
			sysMsg(msgError)
		else:
			sysMsg(msgEnd)


# Starting from stats menu, reincarnate and level up via key stage
def keyLv():
	clkObj(pok_menuBack)
	clkObj(pok_train)
	clkObj(pok_himeRe)
	clkObj(pok_reConfirm)
	clkObj(pok_yes)
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	sleep(double)
	click(atMouse())
	clkObj(pok_btStart)
	clkObj(pok_btResult, changePage, remark = "btResult")
	sleep(double)
	click(atMouse())
	if exists(OK):
		clkObj(pok_OK)
	clkObj(pok_btResult, double, True, remark = "btResult")
	clkObj(pok_loot, double, True)
	clkObj(pok_btEndNext)
	clkObj(pok_keyUnlock)
	clkObj(pok_keyLv3)
	clkObj(pok_yes)
	clkObj(pok_keyStg, changePage)
	clkObj(pok_unit1)
	clkObj(pok_gear1)
	clkObj(pok_egg)
	clkObj(pok_confirm)
	clkObj(pok_stats)