function showUnreleased() {
	var x = document.getElementsByClassName("unreleased");
	var y = document.getElementById("showBtn1");

	if (y.innerText == "顯示未實裝刻印") {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = "table-row";
		}

		y.innerHTML = "隱藏未實裝刻印";
	} else {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = "none";
		}

		y.innerHTML = "顯示未實裝刻印";
	}
}

function showComment() {
	var x = document.getElementById("Comment");

	if (x.style.display == "none") {
		x.style.display = "block";
		document.getElementById("showBtn2").innerHTML = "隱藏";
	} else {
		x.style.display = "none";
		document.getElementById("showBtn2").innerHTML = "顯示";
	}
}

function randomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	x = Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
	console.log("Rolled " + x + " for " + min + " ≤ x ≤ " + max);
	return x;
}

/* Assign random stats to runes */
function randomStat(set, rank, statEmId) { // proabilitySet, runeRank, td#statEmId
	var el = document.getElementById(statEmId);
	var p = parseInt(randomInt(1, 100));
	document.getElementById("rolled").innerHTML = (p + " / 100");
	var output = 0;
	switch (set) {
		case "A":
			if (p > 90) {
				switch (rank) {
					case "ssr":
						output = randomInt(96, 100);
						document.getElementById("range").innerHTML = ("Range: 96 - 100");
						break;
					case "sr":
						output = randomInt(51, 55);
						document.getElementById("range").innerHTML = ("Range: 51 - 55");
						break;
					case "r":
						output = randomInt(21, 25);
						document.getElementById("range").innerHTML = ("Range: 21 - 25");
						break;
				}
			} else if (p > 70) {
				switch (rank) {
					case "ssr":
						output = randomInt(91, 95);
						document.getElementById("range").innerHTML = ("Range: 91 - 95");
						break;
					case "sr":
						output = randomInt(46, 50);
						document.getElementById("range").innerHTML = ("Range: 46 - 50");
						break;
					case "r":
						output = randomInt(16, 20);
						document.getElementById("range").innerHTML = ("Range: 16 - 20");
						break;
				}
			} else if (p > 0) {
				switch (rank) {
					case "ssr":
						output = randomInt(76, 90);
						document.getElementById("range").innerHTML = ("Range: 76 - 90");
						break;
					case "sr":
						output = randomInt(31, 45);
						document.getElementById("range").innerHTML = ("Range: 31 - 45");
						break;
					case "r":
						output = randomInt(1, 15);
						document.getElementById("range").innerHTML = ("Range: 1 - 15");
						break;
				}
			} else {
				console.log("Error in randomStat(" + set + ", " + rank + ", " + statEmId + ") case A, please check.");
			}
			break;
		case "B":
			if (p > 85) {
				switch (rank) {
					case "ssr":
						output = randomInt(651, 700);
						document.getElementById("range").innerHTML = ("Range: 651 - 700");
						break;
					case "sr":
						output = randomInt(371, 420);
						document.getElementById("range").innerHTML = ("Range: 371 - 420");
						break;
					case "r":
						output = randomInt(176, 200);
						document.getElementById("range").innerHTML = ("Range: 176 - 200");
						break;
				}
			} else if (p > 60) {
				switch (rank) {
					case "ssr":
						output = randomInt(601, 650);
						document.getElementById("range").innerHTML = ("Range: 601 - 650");
						break;
					case "sr":
						output = randomInt(321, 370);
						document.getElementById("range").innerHTML = ("Range: 321 - 370");
						break;
					case "r":
						output = randomInt(151, 175);
						document.getElementById("range").innerHTML = ("Range: 151 - 175");
						break;
				}
			} else if (p > 0) {
				switch (rank) {
					case "ssr":
						output = randomInt(501, 600);
						document.getElementById("range").innerHTML = ("Range: 501 - 600");
						break;
					case "sr":
						output = randomInt(221, 320);
						document.getElementById("range").innerHTML = ("Range: 221 - 320");
						break;
					case "r":
						output = randomInt(101, 150);
						document.getElementById("range").innerHTML = ("Range: 101 - 150");
						break;
				}
			} else {
				console.log("Error in randomStat(" + set + ", " + rank + ", " + statEmId + ") case B, please check.");
			}
			break;
		case "C":
			if (p > 98) {
				switch (rank) {
					case "ssr":
						output = 10;
						document.getElementById("range").innerHTML = ("Range: 10 - 10");
						break;
					case "sr":
						output = 6;
						document.getElementById("range").innerHTML = ("Range: 6 - 6");
						break;
					case "r":
						output = 3;
						document.getElementById("range").innerHTML = ("Range: 3 - 3");
						break;
				}
			} else if (p > 83) {
				switch (rank) {
					case "ssr":
						output = 9;
						document.getElementById("range").innerHTML = ("Range: 9 - 9");
						break;
					case "sr":
						output = 5;
						document.getElementById("range").innerHTML = ("Range: 5 - 5");
						break;
					case "r":
						output = 2;
						document.getElementById("range").innerHTML = ("Range: 2 - 2");
						break;
				}
			} else if (p > 0) {
				switch (rank) {
					case "ssr":
						output = 8;
						document.getElementById("range").innerHTML = ("Range: 8 - 8");
						break;
					case "sr":
						output = 4;
						document.getElementById("range").innerHTML = ("Range: 4 - 4");
						break;
					case "r":
						output = 1;
						document.getElementById("range").innerHTML = ("Range: 1 - 1");
						break;
				}
			} else {
				console.log("Error in randomStat(" + set + ", " + rank + ", " + statEmId + ") case C, please check.");
			}
			break;
		default:
			console.log("Error in randomStat(" + set + ", " + rank + ", " + statEmId + "), please check.");
	}
	el.innerHTML = output;
}

function refreshStats() {
	var x1 = +document.getElementById("statEm1").innerHTML;
	var y1 = +document.getElementById("statEn1").innerHTML;
	document.getElementById("statTotal1").innerHTML = x1 + y1;
	var x2 = +document.getElementById("statEm2").innerHTML;
	var y2 = +document.getElementById("statEn2").innerHTML;
	document.getElementById("statTotal2").innerHTML = x2 + y2;
	var x3 = +document.getElementById("statEm3").innerHTML;
	var y3 = +document.getElementById("statEn3").innerHTML;
	document.getElementById("statTotal3").innerHTML = x3 + y3;
	var x4 = +document.getElementById("statEm4").innerHTML;
	var y4 = +document.getElementById("statEn4").innerHTML;
	document.getElementById("statTotal4").innerHTML = x4 + y4;
	var x5 = +document.getElementById("statEm5").innerHTML;
	var y5 = +document.getElementById("statEn5").innerHTML;
	document.getElementById("statTotal5").innerHTML = x5 + y5;
	var x6 = +document.getElementById("statEm6").innerHTML;
	var y6 = +document.getElementById("statEn6").innerHTML;
	document.getElementById("statTotal6").innerHTML = x6 + y6;
}

function lockInput() {
	/* Insert Rune images */
	var rank1 = document.getElementById("rank1").value;
	var set1 = document.getElementById("set1").value.substring(2);
	var ico1 = document.getElementById("set1").value.substring(0, 2);
	document.getElementById("rune1").innerHTML = "<img src='resources/it_rune_" + rank1 + "_1_" + set1 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico1 + ".png>";
	document.getElementById("rune1Em").innerHTML = "<img src='resources/it_rune_" + rank1 + "_1_" + set1 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico1 + ".png>";
	var rank2 = document.getElementById("rank2").value;
	var set2 = document.getElementById("set2").value.substring(2);
	var ico2 = document.getElementById("set2").value.substring(0, 2);
	document.getElementById("rune2").innerHTML = "<img src='resources/it_rune_" + rank2 + "_2_" + set2 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico2 + ".png>";
	document.getElementById("rune2Em").innerHTML = "<img src='resources/it_rune_" + rank2 + "_2_" + set2 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico2 + ".png>";
	var rank3 = document.getElementById("rank3").value;
	var set3 = document.getElementById("set3").value.substring(2);
	var ico3 = document.getElementById("set3").value.substring(0, 2);
	document.getElementById("rune3").innerHTML = "<img src='resources/it_rune_" + rank3 + "_3_" + set3 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico3 + ".png>";
	document.getElementById("rune3Em").innerHTML = "<img src='resources/it_rune_" + rank3 + "_3_" + set3 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico3 + ".png>";
	var rank4 = document.getElementById("rank4").value;
	var set4 = document.getElementById("set4").value.substring(2);
	var ico4 = document.getElementById("set4").value.substring(0, 2);
	document.getElementById("rune4").innerHTML = "<img src='resources/it_rune_" + rank4 + "_4_" + set4 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico4 + ".png>";
	document.getElementById("rune4Em").innerHTML = "<img src='resources/it_rune_" + rank4 + "_4_" + set4 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico4 + ".png>";
	var rank5 = document.getElementById("rank5").value;
	var set5 = document.getElementById("set5").value.substring(2);
	var ico5 = document.getElementById("set5").value.substring(0, 2);
	document.getElementById("rune5").innerHTML = "<img src='resources/it_rune_" + rank5 + "_5_" + set5 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico5 + ".png>";
	document.getElementById("rune5Em").innerHTML = "<img src='resources/it_rune_" + rank5 + "_5_" + set5 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico5 + ".png>";
	var rank6 = document.getElementById("rank6").value;
	var set6 = document.getElementById("set6").value.substring(2);
	var ico6 = document.getElementById("set6").value.substring(0, 2);
	document.getElementById("rune6").innerHTML = "<img src='resources/it_rune_" + rank6 + "_6_" + set6 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico6 + ".png>";
	document.getElementById("rune6Em").innerHTML = "<img src='resources/it_rune_" + rank6 + "_6_" + set6 + ".png'><img class='icon' src=resources/ui_Rune_3_icon_rune_taip" + ico6 + ".png>";

	/* Insert Basic Stat type */
	document.getElementById("stat1").innerHTML = document.querySelector('input[name = "stat1"]:checked').value;
	document.getElementById("stat1Em").innerHTML = document.querySelector('input[name = "stat1"]:checked').value;
	document.getElementById("stat2").innerHTML = document.querySelector('input[name = "stat2"]:checked').value;
	document.getElementById("stat2Em").innerHTML = document.querySelector('input[name = "stat2"]:checked').value;
	document.getElementById("stat4").innerHTML = document.querySelector('input[name = "stat4"]:checked').value;
	document.getElementById("stat4Em").innerHTML = document.querySelector('input[name = "stat4"]:checked').value;
	document.getElementById("stat5").innerHTML = document.querySelector('input[name = "stat5"]:checked').value;
	document.getElementById("stat5Em").innerHTML = document.querySelector('input[name = "stat5"]:checked').value;

	/* Insert Evo Stat type */
	// 嫉妬
	var evo1 = document.getElementById("evo1")
	if (evo1.options[evo1.selectedIndex].value == "idc") {
		document.getElementById("evoStat1").innerHTML = "隨意";
		document.getElementById("evoStat1").className = "idc";
	} else {
		document.getElementById("evoStat1").innerHTML = evo1.options[evo1.selectedIndex].text;
		document.getElementById("evoStat1").className = "pA2";
	}
	// 怠惰
	var evo2 = document.getElementById("evo2")
	if (evo2.options[evo2.selectedIndex].value == "idc") {
		document.getElementById("evoStat2").innerHTML = "隨意";
		document.getElementById("evoStat2").className = "idc";
	} else {
		document.getElementById("evoStat2").innerHTML = evo2.options[evo2.selectedIndex].text;
		document.getElementById("evoStat2").className = "pB2";
	}
	// 色欲
	var evo3 = document.getElementById("evo3")
	if (evo3.options[evo3.selectedIndex].value == "idc") {
		document.getElementById("evoStat3").innerHTML = "隨意";
		document.getElementById("evoStat3").className = "idc";
	} else {
		document.getElementById("evoStat3").innerHTML = evo3.options[evo3.selectedIndex].text;
		document.getElementById("evoStat3").className = "pB2";
	}
	// 暴食
	var evo4 = document.getElementById("evo4")
	if (evo4.options[evo4.selectedIndex].value == "idc") {
		document.getElementById("evoStat4").innerHTML = "隨意";
		document.getElementById("evoStat4").className = "idc";
	} else {
		if (evo4.options[evo4.selectedIndex].value == "mpGainUp") {
			document.getElementById("evoStat4").className = "pB2";
		} else if (evo4.options[evo4.selectedIndex].value == "gutsUp") {
			document.getElementById("evoStat4").className = "pC2";
		} else {
			document.getElementById("evoStat4").className = "pA2";
		}
		document.getElementById("evoStat4").innerHTML = evo4.options[evo4.selectedIndex].text;
	}
	// 憤怒
	var evo5 = document.getElementById("evo5")
	if (evo5.options[evo5.selectedIndex].value == "idc") {
		document.getElementById("evoStat5").innerHTML = "隨意";
		document.getElementById("evoStat5").className = "idc";
	} else {
		document.getElementById("evoStat5").innerHTML = evo5.options[evo5.selectedIndex].text;
		document.getElementById("evoStat5").className = "pB2";
	}
	// 強欲
	var evo6 = document.getElementById("evo6")
	if (evo6.options[evo6.selectedIndex].value == "idc") {
		document.getElementById("evoStat6").innerHTML = "隨意";
		document.getElementById("evoStat6").className = "idc";
	} else {
		document.getElementById("evoStat6").innerHTML = evo6.options[evo6.selectedIndex].text;
		document.getElementById("evoStat6").className = "pB2";
	}

	/* Calculate Set Bonus */
	var setCount = [ico1, ico2, ico3, ico4, ico5, ico6];
	// 強攻
	var kongo = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "00")
			kongo++;
	}
	if (kongo > 3) {
		document.getElementById("setBonus").innerHTML += "物攻+10%<br>";
		document.getElementById("setBonusEm").innerHTML += "物攻+10%<br>";
	}
	// 魔道
	var mado = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "01")
			mado++;
	}
	if (mado > 3) {
		document.getElementById("setBonus").innerHTML += "魔攻+10%<br>";
		document.getElementById("setBonusEm").innerHTML += "魔攻+10%<br>";
	}
	// 堅牢
	var kenro = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "02")
			kenro++;
	}
	if (kenro > 5) {
		document.getElementById("setBonus").innerHTML += "物防+30%<br>";
		document.getElementById("setBonusEm").innerHTML += "物防+30%<br>";
	} else if (kenro > 3) {
		document.getElementById("setBonus").innerHTML += "物防+20%<br>";
		document.getElementById("setBonusEm").innerHTML += "物防+20%<br>";
	} else if (kenro > 1) {
		document.getElementById("setBonus").innerHTML += "物防+10%<br>";
		document.getElementById("setBonusEm").innerHTML += "物防+10%<br>";
	}
	// 魔陣
	var majin = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "03")
			majin++;
	}
	if (majin > 5) {
		document.getElementById("setBonus").innerHTML += "魔防+30%<br>";
		document.getElementById("setBonusEm").innerHTML += "魔防+30%<br>";
	} else if (majin > 3) {
		document.getElementById("setBonus").innerHTML += "魔防+20%<br>";
		document.getElementById("setBonusEm").innerHTML += "魔防+20%<br>";
	} else if (majin > 1) {
		document.getElementById("setBonus").innerHTML += "魔防+10%<br>";
		document.getElementById("setBonusEm").innerHTML += "魔防+10%<br>";
	}
	// 命脈
	var meimyaku = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "07")
			meimyaku++;
	}
	if (meimyaku > 3) {
		document.getElementById("setBonus").innerHTML += "HP+15%<br>";
		document.getElementById("setBonusEm").innerHTML += "HP+15%<br>";
	}
	// 一閃
	var issen = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "11")
			issen++;
	}
	if (issen > 5) {
		document.getElementById("setBonus").innerHTML += "単体攻擊+15<br>";
		document.getElementById("setBonusEm").innerHTML += "単体攻擊+15<br>";
	} else if (issen > 3) {
		document.getElementById("setBonus").innerHTML += "単体攻擊+10<br>";
		document.getElementById("setBonusEm").innerHTML += "単体攻擊+10<br>";
	} else if (issen > 1) {
		document.getElementById("setBonus").innerHTML += "単体攻擊+5<br>";
		document.getElementById("setBonusEm").innerHTML += "単体攻擊+5<br>";
	}
	// 一掃
	var isso = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "12")
			isso++;
	}
	if (isso > 5) {
		document.getElementById("setBonus").innerHTML += "範囲攻擊+15<br>";
		document.getElementById("setBonusEm").innerHTML += "範囲攻擊+15<br>";
	} else if (isso > 3) {
		document.getElementById("setBonus").innerHTML += "範囲攻擊+10<br>";
		document.getElementById("setBonusEm").innerHTML += "範囲攻擊+10<br>";
	} else if (isso > 1) {
		document.getElementById("setBonus").innerHTML += "範囲攻擊+5<br>";
		document.getElementById("setBonusEm").innerHTML += "範囲攻擊+5<br>";
	}

	/* Switch display style parameter */
	document.getElementById("inputValue").style.display = "none";
	document.getElementById("outputTable").style.display = "block";

	/* Assign random basic stats */
	randomStat("A", rank1, "statEm1");
	randomStat("A", rank2, "statEm2");
	randomStat("B", rank3, "statEm3");
	randomStat("A", rank4, "statEm4");
	randomStat("A", rank5, "statEm5");
	randomStat("C", rank6, "statEm6");
	refreshStats();
}

function evoStatInt(set, evoStatIntEmId) {
	var evoInt = document.getElementById(evoStatIntEmId);
	switch (set) {
		case "A":
			var roll = randomInt(1, 100);
			document.getElementById("rolled").innerHTML = (roll + " / 100");
			evoInt.className = "pA2";
			if (roll > 98) {
				evoInt.innerHTML = 5;
				document.getElementById("range").innerHTML = ("Range: 5 - 5");
			} else if (roll > 90) {
				evoInt.innerHTML = 4;
				document.getElementById("range").innerHTML = ("Range: 4 - 4");
			} else if (roll > 70) {
				evoInt.innerHTML = 3;
				document.getElementById("range").innerHTML = ("Range: 3 - 3");
			} else if (roll > 40) {
				evoInt.innerHTML = 2;
				document.getElementById("range").innerHTML = ("Range: 2 - 2");
			} else if (roll > 0) {
				evoInt.innerHTML = 1;
				document.getElementById("range").innerHTML = ("Range: 1 - 1");
			} else {
				console.log("Error in evoStatInt(" + set + ", " + evoStatIntEmId + ") case A, please check.");
			}
			break;
		case "B":
			var roll = randomInt(1, 100);
			document.getElementById("rolled").innerHTML = (roll + " / 100");
			evoInt.className = "pB2";
			if (roll > 98) {
				document.getElementById(evoStatIntEmId).innerHTML = randomInt(9, 10);
				document.getElementById("range").innerHTML = ("Range: 9 - 10");
			} else if (roll > 90) {
				document.getElementById(evoStatIntEmId).innerHTML = randomInt(7, 8);
				document.getElementById("range").innerHTML = ("Range: 7 - 8");
			} else if (roll > 70) {
				document.getElementById(evoStatIntEmId).innerHTML = randomInt(5, 6);
				document.getElementById("range").innerHTML = ("Range: 5 - 6");
			} else if (roll > 40) {
				document.getElementById(evoStatIntEmId).innerHTML = randomInt(3, 4);
				document.getElementById("range").innerHTML = ("Range: 3 - 4");
			} else if (roll > 0) {
				document.getElementById(evoStatIntEmId).innerHTML = randomInt(1, 2);
				document.getElementById("range").innerHTML = ("Range: 1 - 2");
			} else {
				console.log("Error in evoStatInt(" + set + ", " + evoStatIntEmId + ") case B, please check.");
			}
			break;
		case "C":
			var roll = randomInt(1, 90);
			document.getElementById("rolled").innerHTML = (roll + " / 90");
			evoInt.className = "pC2";
			console.log(roll);
			if (roll > 70) {
				document.getElementById(evoStatIntEmId).innerHTML = 3;
				document.getElementById("range").innerHTML = ("Range: 3 - 3");
			} else if (roll > 40) {
				document.getElementById(evoStatIntEmId).innerHTML = 2;
				document.getElementById("range").innerHTML = ("Range: 2 - 2");
			} else if (roll > 0) {
				document.getElementById(evoStatIntEmId).innerHTML = 1;
				document.getElementById("range").innerHTML = ("Range: 1 - 1");
			} else {
				console.log("Error in evoStatInt(" + set + ", " + evoStatIntEmId + ") case C, please check.");
			}
			break;
		default:
			console.log("Error in evoStatInt(" + set + ", " + evoStatIntEmId + "), please check.");
	}
}

function evoStat(slot, evoStatEmId, evoStatIntEmId) { // slot, tdId(#evoStat), tdId(#evoStatIntEm)
	var evoType = document.getElementById(evoStatEmId);
	switch (slot) { //slot is string
		case "1": //嫉妬
			var roll = randomInt(1, 6);
			evoType.className = "pA2";
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "斬擊攻擊";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "打擊攻擊";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "刺突攻擊";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "射撃攻擊";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "魔法攻擊";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "跳躍攻擊";
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 1, please check.");
			}
			evoStatInt("A", evoStatIntEmId);
			break;
		case "2": //怠惰
			var roll = randomInt(1, 6);
			evoType.className = "pB2";
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "斬擊耐性";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "打擊耐性";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "刺突耐性";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "射撃耐性";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "魔法耐性";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "跳躍耐性";
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 2, please check.");
			}
			evoStatInt("B", evoStatIntEmId);
			break;
		case "3": //色欲
			var roll = randomInt(1, 8);
			evoType.className = "pB2";
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "毒耐性";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "暈眩耐性";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "麻痺耐性";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "睡眠耐性";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "魅了耐性";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "狂化耐性";
					break;
				case 7:
					document.getElementById(evoStatEmId).innerHTML = "Clockdown耐性";
					break;
				case 8:
					document.getElementById(evoStatEmId).innerHTML = "鈍足耐性";
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 3, please check.");
			}
			evoStatInt("B", evoStatIntEmId);
			break;
		case "4": //暴食
			var roll = randomInt(1, 5);
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "MP回復";
					evoType.className = "pA2";
					evoStatInt("A", evoStatIntEmId);
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "最大MP";
					evoType.className = "pB2";
					evoStatInt("B", evoStatIntEmId);
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "治癒力";
					evoType.className = "pA2";
					evoStatInt("A", evoStatIntEmId);
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "根性";
					evoType.className = "pC2";
					evoStatInt("C", evoStatIntEmId);
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "暴擊率";
					evoType.className = "pA2";
					evoStatInt("A", evoStatIntEmId);
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 4, please check.");
			}
			break;
		case "5": //憤怒
			var roll = randomInt(1, 7);
			evoType.className = "pB2";
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "物攻衰弱耐性";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "物防衰弱耐性";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "魔攻衰弱耐性";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "魔防衰弱耐性";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "器用衰弱耐性";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "素早衰弱耐性";
					break;
				case 7:
					document.getElementById(evoStatEmId).innerHTML = "運衰弱耐性";
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 5, please check.");
			}
			evoStatInt("B", evoStatIntEmId);
			break;
		case "6": //強欲
			var roll = randomInt(1, 8);
			evoType.className = "pB2";
			switch (roll) {
				case 1:
					document.getElementById(evoStatEmId).innerHTML = "毒耐性";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "暈眩耐性";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "麻痺耐性";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "睡眠耐性";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "魅了耐性";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "狂化耐性";
					break;
				case 7:
					document.getElementById(evoStatEmId).innerHTML = "Clockdown耐性";
					break;
				case 8:
					document.getElementById(evoStatEmId).innerHTML = "鈍足耐性";
					break;
				default:
					console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + ") case 6, please check.");
			}
			evoStatInt("B", evoStatIntEmId);
			break;
		default:
			console.log("Error in evoStat(" + slot + ", " + evoStatEmId + ", " + evoStatIntEmId + "), please check.");
	}
}

function enchance(enRate, lv, quality) {
	var roll = randomInt(1, 100);
	document.getElementById("rolled").innerHTML = (roll + " / 100");
	var baseRate = parseInt(document.getElementById(enRate).innerHTML);
	if (roll > (100 - baseRate)) {
		document.getElementById("range").innerHTML = "成功";
		return true;
	} else {
		var failedBonus = 0;
		var evo = document.getElementById(lv).innerHTML.substring(2, 3);
		switch (quality) {
			case "ssr":
				switch (evo) {
					case "1":
						failedBonus = 5;
						break;
					case "2":
						failedBonus = 10;
						break;
					case "3":
						failedBonus = 15;
						break;
				}
				break;
			case "sr":
				switch (evo) {
					case "1":
						failedBonus = 4;
						break;
					case "2":
						failedBonus = 8;
						break;
					case "3":
						failedBonus = 12;
						break;
				}
				break;
			case "r":
				switch (evo) {
					case "1":
						failedBonus = 3;
						break;
					case "2":
						failedBonus = 6;
						break;
					case "3":
						failedBonus = 9;
						break;
				}
				break;
			default:
				console.log("Error in enchance(" + enRate + ", " + lv + ", " + quality + "), please check.");
		}
		newBaseRate = parseInt(baseRate) + parseInt(failedBonus);
		document.getElementById(enRate).innerHTML = (newBaseRate + "%");
		document.getElementById("range").innerHTML = "失敗";
		return false;
	}
}

function upgrade(set, slot) {
	var statEnId = document.getElementById("statEn" + slot);
	var level = document.getElementById("lv" + slot);
	var quality = document.getElementById("rank" + slot).value;
	var enRate = "enRate" + slot;
	var btn = document.getElementById("en" + slot);
	var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
	var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
	var roll = randomInt(1, 100);
	document.getElementById("rolled").innerHTML = (roll + " / 100");
	var output = statEnId.innerHTML;
	var cost = 0;

	switch (level.innerHTML) {
		case "覺醒0 強化0":
			switch (quality) {
				case "ssr":
					cost = 90000;
					break;
				case "sr":
					cost = 60000;
					break;
				case "r":
					cost = 30000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 3;
						break;
					case "B":
						output = 10;
						break;
					case "C":
						output = 0;
						break;
				}
				level.innerHTML = "覺醒0 強化1";
			}
			break;
		case "覺醒0 強化1":
			switch (quality) {
				case "ssr":
					cost = 180000;
					break;
				case "sr":
					cost = 120000;
					break;
				case "r":
					cost = 60000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 5;
						break;
					case "B":
						output = 20;
						break;
					case "C":
						output = 0;
						break;
				}
				level.innerHTML = "覺醒0 強化2";
			}
			break;
		case "覺醒0 強化2":
			switch (quality) {
				case "ssr":
					cost = 270000;
					break;
				case "sr":
					cost = 180000;
					break;
				case "r":
					cost = 90000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 7;
						break;
					case "B":
						output = 30;
						break;
					case "C":
						output = 1;
						break;
				}
				level.innerHTML = "覺醒0 強化3";
				btn.innerHTML = "覺醒";
				btn.className = "ev";
			}
			break;
		case "覺醒0 強化3": //覺醒
			switch (quality) {
				case "ssr":
					cost = 1500000;
					break;
				case "sr":
					cost = 1000000;
					break;
				case "r":
					cost = 500000;
					break;
			}
			level.innerHTML = "覺醒1 強化0";
			btn.innerHTML = "強化";
			document.getElementById(enRate).innerHTML = "60%";
			btn.className = "en";
			evoStat(slot, "evoStatEm" + "1" + slot, "evoStatIntEm" + "1" + slot);
			break;
		case "覺醒1 強化0":
			switch (quality) {
				case "ssr":
					cost = 360000;
					break;
				case "sr":
					cost = 240000;
					break;
				case "r":
					cost = 120000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 9;
						break;
					case "B":
						output = 40;
						break;
					case "C":
						output = 1;
						break;
				}
				level.innerHTML = "覺醒1 強化1";
				document.getElementById(enRate).innerHTML = "60%";
			}
			break;
		case "覺醒1 強化1":
			switch (quality) {
				case "ssr":
					cost = 450000;
					break;
				case "sr":
					cost = 300000;
					break;
				case "r":
					cost = 150000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 11;
						break;
					case "B":
						output = 50;
						break;
					case "C":
						output = 1;
						break;
				}
				level.innerHTML = "覺醒1 強化2";
				document.getElementById(enRate).innerHTML = "60%";
			}
			break;
		case "覺醒1 強化2":
			switch (quality) {
				case "ssr":
					cost = 540000;
					break;
				case "sr":
					cost = 360000;
					break;
				case "r":
					cost = 180000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 13;
						break;
					case "B":
						output = 60;
						break;
					case "C":
						output = 2;
						break;
				}
				level.innerHTML = "覺醒1 強化3";
				btn.innerHTML = "覺醒";
				btn.className = "ev";
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒1 強化3": //覺醒
			switch (quality) {
				case "ssr":
					cost = 3000000;
					break;
				case "sr":
					cost = 2000000;
					break;
				case "r":
					cost = 1000000;
					break;
			}
			level.innerHTML = "覺醒2 強化0";
			btn.innerHTML = "強化";
			document.getElementById(enRate).innerHTML = "30%";
			btn.className = "en";
			evoStat(slot, "evoStatEm" + "2" + slot, "evoStatIntEm" + "2" + slot);
		case "覺醒2 強化0":
			switch (quality) {
				case "ssr":
					cost = 630000;
					break;
				case "sr":
					cost = 420000;
					break;
				case "r":
					cost = 210000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 15;
						break;
					case "B":
						output = 70;
						break;
					case "C":
						output = 2;
						break;
				}
				level.innerHTML = "覺醒2 強化1";
				document.getElementById(enRate).innerHTML = "30%";
			}
			break;
		case "覺醒2 強化1":
			switch (quality) {
				case "ssr":
					cost = 720000;
					break;
				case "sr":
					cost = 480000;
					break;
				case "r":
					cost = 240000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 17;
						break;
					case "B":
						output = 80;
						break;
					case "C":
						output = 2;
						break;
				}
			level.innerHTML = "覺醒2 強化2";
			document.getElementById(enRate).innerHTML = "30%";
			}
			break;
		case "覺醒2 強化2":
			switch (quality) {
				case "ssr":
					cost = 810000;
					break;
				case "sr":
					cost = 540000;
					break;
				case "r":
					cost = 270000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 19;
						break;
					case "B":
						output = 90;
						break;
					case "C":
						output = 3;
						break;
				}
				level.innerHTML = "覺醒2 強化3";
				btn.innerHTML = "覺醒";
				btn.className = "ev";
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒2 強化3": //覺醒
			switch (quality) {
				case "ssr":
					cost = 4500000;
					break;
				case "sr":
					cost = 3000000;
					break;
				case "r":
					cost = 1500000;
					break;
			}
			level.innerHTML = "覺醒3 強化0";
			btn.innerHTML = "強化";
			document.getElementById(enRate).innerHTML = "10%";
			btn.className = "en";
			evoStat(slot, "evoStatEm" + "3" + slot, "evoStatIntEm" + "3" + slot);
			break;
		case "覺醒3 強化0":
			switch (quality) {
				case "ssr":
					cost = 900000;
					break;
				case "sr":
					cost = 600000;
					break;
				case "r":
					cost = 300000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 21;
						break;
					case "B":
						output = 100;
						break;
					case "C":
						output = 3;
						break;
				}
				level.innerHTML = "覺醒3 強化1";
				document.getElementById(enRate).innerHTML = "10%";
			}
			break;
		case "覺醒3 強化1":
			switch (quality) {
				case "ssr":
					cost = 990000;
					break;
				case "sr":
					cost = 660000;
					break;
				case "r":
					cost = 330000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 23;
						break;
					case "B":
						output = 110;
						break;
					case "C":
						output = 3;
						break;
				}
				level.innerHTML = "覺醒3 強化2";
				document.getElementById(enRate).innerHTML = "10%";
			}
			break;
		case "覺醒3 強化2":
			switch (quality) {
				case "ssr":
					cost = 1080000;
					break;
				case "sr":
					cost = 720000;
					break;
				case "r":
					cost = 360000;
					break;
			}
			if (enchance("enRate" + slot, "lv" + slot, quality) == true) {
				switch (set) {
					case "A":
						output = 25;
						break;
					case "B":
						output = 120;
						break;
					case "C":
						switch (quality) {
							case "ssr":
								output = 5;
								break;
							case "sr":
							case "r":
								output = 4;
								break;
						}
						break;
				}
				level.innerHTML = "覺醒3 強化3";
				btn.style.display = "none";
				document.getElementById(enRate).innerHTML = "N/A";
			}
			break;
		default:
			console.log("Error in upgrade(" + set + ", " + slot + "), please check.");
	}
	statEnId.innerHTML = output
	document.getElementById("zeni").innerHTML = Intl.NumberFormat('en-US').format(zeni + cost);
	refreshStats();
}

function rerollBasic(set, slot) {
	var quality = document.getElementById("rank" + slot).value;
	var statEmId = ("statEm" + slot);
	randomStat(set, quality, statEmId);
	refreshStats();

	var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
	var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
	switch (quality) {
		case "ssr":
			document.getElementById("gem").innerHTML = Intl.NumberFormat('en-US').format(gem + 200);
			break;
		case "sr":
			document.getElementById("zeni").innerHTML = Intl.NumberFormat('en-US').format(zeni + 600000);
			break;
		case "r":
			document.getElementById("zeni").innerHTML = Intl.NumberFormat('en-US').format(zeni + 300000);
			break;
	}
}

function rerollEvo(row, slot) {
	var evoStatEmId = "evoStatEm" + row + slot;
	var evoStatIntEmId = "evoStatIntEm" + row + slot;
	if (document.getElementById(evoStatEmId).innerHTML == "N/A") {
		console.log("Invalid level");
	} else {
		var quality = document.getElementById("rank" + slot).value;
		evoStat(slot, evoStatEmId, evoStatIntEmId);
		refreshStats();

		var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
		var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
		switch (quality) {
			case "ssr":
				document.getElementById("gem").innerHTML = Intl.NumberFormat('en-US').format(gem + 200);
				break;
			case "sr":
				document.getElementById("gem").innerHTML = Intl.NumberFormat('en-US').format(gem + 100);
				break;
			case "r":
				document.getElementById("zeni").innerHTML = Intl.NumberFormat('en-US').format(zeni + 500000);
				break;
		}
	}
}
