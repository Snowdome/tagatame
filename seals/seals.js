function showNote() {
	var x = document.getElementById("history");

	if (x.style.display == "none") {
		x.style.display = "table-row-group";
		document.getElementById("showBtn").innerHTML = "Hide update history";
	} else {
		x.style.display = "none";
		document.getElementById("showBtn").innerHTML = "Show update history";
	}
}

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

function switchTable4Btn() {
	if (document.getElementById("switchTable4").innerHTML == "顯示01/06/2021前版本" ){
		document.getElementById("switchTable4").innerHTML = "顯示01/06/2021後版本";
		document.getElementById("table4").style.display = "table";
		document.getElementById("table4v2").style.display = "none";
	} else {
		document.getElementById("switchTable4").innerHTML = "顯示01/06/2021前版本"
		document.getElementById("table4").style.display = "none";
		document.getElementById("table4v2").style.display = "table";
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

function selectedText(selectId) {
	return selectId.options[selectId.selectedIndex].text
}

/* function saveAs(uri, filename) {
	var link = document.createElement('a');
	if (typeof link.download === 'string') {
		document.body.appendChild(link);	//Firefox requires the link to be in the body
		link.download = filename;
		link.href = uri;
		link.click();
		document.body.removeChild(link);	// remove the link when done
	} else {
		location.replace(uri);
	}
} */

function convertToPNG() {
	document.getElementById("convertToPNG").disabled = true;
	html2canvas(document.getElementById("table8")).then(function(canvas) {
		document.getElementById("canvasOutput").appendChild(canvas);
		document.getElementsByTagName("canvas")[0].setAttribute("id", "canvasRune");
		var image = canvasRune.toDataURL("image/png");
		document.getElementById("canvasOutput").href = image;
	});
	document.getElementById("outputTable").style.display = "none";
}

function createJSON() {
	var data = {
		"title": document.getElementById("title").value,
		"rune1": [
			set1.options[set1.selectedIndex].text,
			document.getElementById("rank1").value,
			document.getElementById("stat1").innerText,
			document.getElementById("stat1Given").value,
			document.getElementById("evo1").value
		],
		"rune2": [
			set2.options[set2.selectedIndex].text,
			document.getElementById("rank2").value,
			document.getElementById("stat2").innerText,
			document.getElementById("stat2Given").value,
			document.getElementById("evo2").value
		],
		"rune3": [
			set3.options[set3.selectedIndex].text,
			document.getElementById("rank3").value,
			document.getElementById("stat3").innerText,
			document.getElementById("stat3Given").value,
			document.getElementById("evo3").value
		],
		"rune4": [
			set4.options[set4.selectedIndex].text,
			document.getElementById("rank4").value,
			document.getElementById("stat4").innerText,
			document.getElementById("stat4Given").value,
			document.getElementById("evo4").value
		],
		"rune5": [
			set5.options[set5.selectedIndex].text,
			document.getElementById("rank5").value,
			document.getElementById("stat5").innerText,
			document.getElementById("stat5Given").value,
			document.getElementById("evo5").value
		],
		"rune6": [
			set6.options[set6.selectedIndex].text,
			document.getElementById("rank6").value,
			document.getElementById("stat6").innerText,
			document.getElementById("stat6Given").value,
			document.getElementById("evo6").value
		]
	}
	return data;
}

function importJSON() {
	var runeSet = JSON.parse(document.getElementById("jsonOutput").value);
	document.getElementById("title").value = runeSet.title;
	for (r = 1; r < 7; r++) {
		/* Import title */
		var runeSlot = "rune" + r;
		var stat = "stat" + r;
		/* Array[0] - 符文 */
		switch (runeSet[runeSlot][0]) {
			case "強攻":
				document.getElementById("set" + r).value = "00kongo";
				break;
			case "魔道":
				document.getElementById("set" + r).value = "01mado";
				break;
			case "堅牢":
				document.getElementById("set" + r).value = "02kenro";
				break;
			case "魔陣":
				document.getElementById("set" + r).value = "03majin";
				break;
			case "加護":
				document.getElementById("set" + r).value = "05kago";
				break;
			case "宝石":
				document.getElementById("set" + r).value = "06houseki";
				break;
			case "命脈":
				document.getElementById("set" + r).value = "07meimyaku";
				break;
			case "一閃":
				document.getElementById("set" + r).value = "11issen";
				break;
			case "一掃":
				document.getElementById("set" + r).value = "12isso";
				break;
			default:
				alert("Given data is corrupted - " + runeSlot + "$符文");
				console.log(runeSet[runeSlot][0]);
		}
		/* Array[1] - 刻印級別 */
		switch (runeSet[runeSlot][1]) {
			case "ssr":
			case "sr":
			case "r":
				document.getElementById("rank" + r).value = runeSet[runeSlot][1];
				break;
			default:
				alert("Given data is corrupted - " + runeSlot + "$刻印級別");
				console.log(runeSet[runeSlot][1]);
		}
		/* Array[2] - 基礎屬性 */
		switch (r) {
			case 1:
				if (runeSet[runeSlot][2] == "物攻") {
					document.getElementById(stat + "_patk").checked = true;
				} else if (runeSet[runeSlot][2] == "器用") {
					document.getElementById(stat + "_dex").checked = true;
				} else {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			case 2:
				if (runeSet[runeSlot][2] == "物防") {
					document.getElementById(stat + "_pdef").checked = true;
				} else if (runeSet[runeSlot][2] == "会心") {
					document.getElementById(stat + "_crit").checked = true;
				} else {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			case 3:
				if (runeSet[runeSlot][2] != "HP") {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			case 4:
				if (runeSet[runeSlot][2] == "魔攻") {
					document.getElementById(stat + "_matk").checked = true;
				} else if (runeSet[runeSlot][2] == "器用") {
					document.getElementById(stat + "_dex").checked = true;
				} else {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			case 5:
				if (runeSet[runeSlot][2] == "魔防") {
					document.getElementById(stat + "_mdef").checked = true;
				} else if (runeSet[runeSlot][2] == "運") {
					document.getElementById(stat + "_luck").checked = true;
				} else {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			case 6:
				if (runeSet[runeSlot][2] != "素早") {
					alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
					console.log(runeSet[runeSlot][2]);
				}
				break;
			default:
				alert("Given data is corrupted - " + runeSlot + "$基礎屬性");
				console.log(runeSet[runeSlot][2]);
		}
		/* Array[3] - 基礎數值 */
		document.getElementById(stat + "Given").value = runeSet[runeSlot][3];
		/* Array[4] - 覺醒屬性 */
		document.getElementById("evo" + r).value = runeSet[runeSlot][4];
	}
	console.log("Imported JSON");
}

function downloadJSON() {
	var universalBOM = "\uFEFF";
	var data = createJSON();
	document.getElementById("jsonOutput").value = JSON.stringify(data);
	document.getElementById("jsonOutput").setAttribute("data-export", JSON.stringify(data));

	// The download function takes a CSV string, the filename and mimeType as parameters
	// Scroll/look down at the bottom of this snippet to see how download is called
	var download = function(content, fileName, mimeType) {
		var a = document.createElement('a');
		mimeType = mimeType || 'application/octet-stream';

		if (navigator.msSaveBlob) { // IE10
			navigator.msSaveBlob(new Blob([content], {
				type: mimeType
			}), fileName);
		} else if (URL && 'download' in a) { //html5 A[download]
			a.href = URL.createObjectURL(new Blob([content], {
				type: mimeType
			}));
			a.setAttribute('download', fileName);
			document.body.appendChild(a);
			a.click();
			document.body.removeChild(a);
		} else {
			location.href = 'data:application/octet-stream,' + encodeURIComponent(content); // only this mime type is supported
		}
	}
	document.getElementById("jsonOutput").value = JSON.stringify(data);
	download(universalBOM + JSON.stringify(data), 'rune.json', 'application/json;encoding:utf-8');
}

function randomInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	x = Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive
	console.log("Rolled " + x + " for " + min + " ≤ x ≤ " + max);
	return x;
}

/* Assign random stats to runes */ // proabilitySet, runeRank, slot
function randomStat(set, rank, slot) {
	console.log("Assigning random stat for rune" + slot + ".");
	var p = parseInt(randomInt(1, 100));
	document.getElementById("rolled").innerHTML = (p + " / 100");
	var output;
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
				console.log("Error in randomStat(" + set + ", " + rank + ", " + slot + ") case A, please check.");
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
				console.log("Error in randomStat(" + set + ", " + rank + ", " + slot + ") case B, please check.");
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
				console.log("Error in randomStat(" + set + ", " + rank + ", " + slot + ") case C, please check.");
			}
			break;
		default:
			console.log("Error in randomStat(" + set + ", " + rank + ", " + slot + "), please check.");
	}
	document.getElementById("stat" + slot + "Em").innerHTML = output;
}

function refreshMinMax(set, slot) {
	var rank = document.getElementById("rank" + slot).value;
	var statIdGiven = "stat" + slot + "Given";
	switch (rank) {
		case "ssr":
			switch (set) {
				case "A":
					document.getElementById(statIdGiven).min = "76";
					document.getElementById(statIdGiven).max = "100";
					break;
				case "B":
					document.getElementById(statIdGiven).min = "501";
					document.getElementById(statIdGiven).max = "700";
					break;
				case "C":
					document.getElementById(statIdGiven).min = "8";
					document.getElementById(statIdGiven).max = "10";
					break;
			}
			break;
		case "sr":
			switch (set) {
				case "A":
					document.getElementById(statIdGiven).min = "31";
					document.getElementById(statIdGiven).max = "55";
					break;
				case "B":
					document.getElementById(statIdGiven).min = "221";
					document.getElementById(statIdGiven).max = "420";
					break;
				case "C":
					document.getElementById(statIdGiven).min = "4";
					document.getElementById(statIdGiven).max = "6";
					break;
			}
			break;
		case "r":
			switch (set) {
				case "A":
					document.getElementById(statIdGiven).min = "1";
					document.getElementById(statIdGiven).max = "25";
					break;
				case "B":
					document.getElementById(statIdGiven).min = "101";
					document.getElementById(statIdGiven).max = "200";
					break;
				case "C":
					document.getElementById(statIdGiven).min = "1";
					document.getElementById(statIdGiven).max = "3";
					break;
			}
			break;
		default:
			console.log("Error in refreshMinMax(" + set + ", " + slot + "), please check.");
	}
}

function refreshStats() {
	for (slot = 1; slot <= 6; slot++) {
		var statEm = parseInt(document.getElementById("stat" + slot + "Em").innerHTML);
		var statEn = parseInt(document.getElementById("statEn" + slot).innerHTML);
		document.getElementById("statTotal" + slot).innerHTML = statEm + statEn;
	}
}

function unlockInput() {
	// Switch display style parameter
	document.getElementById("inputValue").style.display = "block";
	document.getElementById("outputTable").style.display = "none";
	document.getElementById("emulator").style.display = "none";
	document.getElementById("lock").style.display = "inline-block";
	document.getElementById("unlock").style.display = "none";
	document.getElementById("importJSON").style.display = "inline-block";
	document.getElementById("downloadJSON").style.display = "none";
	document.getElementById("setBonus").innerHTML = "";
	
	// Remove of existing canvas, if any
	if (document.getElementsByTagName("canvas")[0] != null) {
		document.getElementsByTagName("canvas")[0].remove();
		document.getElementById("convertToPNG").style.display = "none";
	}

	// Revert outputTable to default values
	for (i = 1; i <= 3; i++) {
		for (j = 1; j <= 6; j++) {
			var evoStatEm = "evoStatEm" + i + j;
			var evoStatIntEm = "evoStatIntEm" + i + j;
			document.getElementById(evoStatEm).innerHTML = "N/A";
			document.getElementById(evoStatIntEm).innerHTML = "N/A";
		}
	}
	for (i=1; i <= 6; i++) {
		var en = "en" + i;
		document.getElementById(en).style.display = "inline-block";
	}
	document.getElementById("zeni").innerHTML = 0;
	document.getElementById("stoneGreen").innerHTML = 0;
	document.getElementById("stoneBlue").innerHTML = 0;
	document.getElementById("stoneYellow").innerHTML = 0;
	document.getElementById("stoneRed").innerHTML = 0;
}

function lockInput() {
	/* Switch display style parameter */
	document.getElementById("inputValue").style.display = "none";
	document.getElementById("outputTable").style.display = "block";
	document.getElementById("emulator").style.display = "block";
	document.getElementById("lock").style.display = "none";
	document.getElementById("unlock").style.display = "inline-block";
	document.getElementById("importJSON").style.display = "none";
	document.getElementById("downloadJSON").style.display = "inline-block";
	document.getElementById("convertToPNG").disabled = false;
	document.getElementById("convertToPNG").style.display = "inline-block";

	/* If title is available, insert title, else cleanup template */
	if (document.getElementById("title").value == "標題") {
		document.getElementById("title").value = "";
		console.log("No title has been input.")
	} else {
		document.getElementById("outputTitle").innerHTML = document.getElementById("title").value;
	}

	/* Insert Rune images */
	for (slot = 1; slot <= 6; slot++) {
		var rank = document.getElementById("rank" + slot).value;
		switch (rank) {
			case "ssr":
				document.getElementById("useGauge" + slot).className = "useGauge5";
				break;
			case "sr":
				document.getElementById("useGauge" + slot).className = "useGauge4";
				break;
			case "r":
				document.getElementById("useGauge" + slot).className = "useGauge3";
				break;
		}
		var set = document.getElementById("set" + slot).value.substring(2);
		var ico = document.getElementById("set" + slot).value.substring(0, 2);
		document.getElementById("rune" + slot).innerHTML = "<img src='../res/seals/it_rune_" + rank + "_1_" + set + ".png'><img class='icon' src=../res/seals/ui_Rune_3_icon_rune_taip" + ico + ".png>";
		document.getElementById("rune" + slot + "Em").innerHTML = "<img src='../res/seals/it_rune_" + rank + "_1_" + set + ".png'><img class='icon' src=../res/seals/ui_Rune_3_icon_rune_taip" + ico + ".png>";
	}

	/* Insert Basic Stat type */
	document.getElementById("stat1").innerHTML = document.querySelector('input[name = "stat1"]:checked').value;
	document.getElementById("statType1").innerHTML = document.querySelector('input[name = "stat1"]:checked').value;
	document.getElementById("stat2").innerHTML = document.querySelector('input[name = "stat2"]:checked').value;
	document.getElementById("statType2").innerHTML = document.querySelector('input[name = "stat2"]:checked').value;
	document.getElementById("stat4").innerHTML = document.querySelector('input[name = "stat4"]:checked').value;
	document.getElementById("statType4").innerHTML = document.querySelector('input[name = "stat4"]:checked').value;
	document.getElementById("stat5").innerHTML = document.querySelector('input[name = "stat5"]:checked').value;
	document.getElementById("statType5").innerHTML = document.querySelector('input[name = "stat5"]:checked').value;

	/* Insert Evo Stat type */
	// 嫉妬
	var evo1 = document.getElementById("evo1")
	if (evo1.options[evo1.selectedIndex].value == "any") {
		document.getElementById("evoStat1").innerHTML = "隨機";
		document.getElementById("evoStat1").className = "any";
	} else {
		document.getElementById("evoStat1").innerHTML = evo1.options[evo1.selectedIndex].text;
		document.getElementById("evoStat1").className = "pA2";
	}
	// 怠惰
	var evo2 = document.getElementById("evo2")
	if (evo2.options[evo2.selectedIndex].value == "any") {
		document.getElementById("evoStat2").innerHTML = "隨機";
		document.getElementById("evoStat2").className = "any";
	} else {
		document.getElementById("evoStat2").innerHTML = evo2.options[evo2.selectedIndex].text;
		document.getElementById("evoStat2").className = "pB2";
	}
	// 色欲
	var evo3 = document.getElementById("evo3")
	if (evo3.options[evo3.selectedIndex].value == "any") {
		document.getElementById("evoStat3").innerHTML = "隨機";
		document.getElementById("evoStat3").className = "any";
	} else {
		document.getElementById("evoStat3").innerHTML = evo3.options[evo3.selectedIndex].text;
		document.getElementById("evoStat3").className = "pB2";
	}
	// 暴食
	var evo4 = document.getElementById("evo4")
	if (evo4.options[evo4.selectedIndex].value == "any") {
		document.getElementById("evoStat4").innerHTML = "隨機";
		document.getElementById("evoStat4").className = "any";
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
	if (evo5.options[evo5.selectedIndex].value == "any") {
		document.getElementById("evoStat5").innerHTML = "隨機";
		document.getElementById("evoStat5").className = "any";
	} else {
		document.getElementById("evoStat5").innerHTML = evo5.options[evo5.selectedIndex].text;
		document.getElementById("evoStat5").className = "pB2";
	}
	// 強欲
	var evo6 = document.getElementById("evo6")
	if (evo6.options[evo6.selectedIndex].value == "any") {
		document.getElementById("evoStat6").innerHTML = "隨機";
		document.getElementById("evoStat6").className = "any";
	} else {
		document.getElementById("evoStat6").innerHTML = evo6.options[evo6.selectedIndex].text;
		document.getElementById("evoStat6").className = "pB2";
	}

	/* Calculate Set Bonus */
	function runeIco(slot) {
		return document.getElementById("set" + slot).value.substring(0, 2);
	}
	var setCount = [runeIco(1), runeIco(2), runeIco(3), runeIco(4), runeIco(5), runeIco(6)];
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
	// 加護
	var kago = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "05")
			kago++;
	}
	if (kago > 5) {
		document.getElementById("setBonus").innerHTML += "全狀態異常耐性+15<br>";
		document.getElementById("setBonusEm").innerHTML += "全狀態異常耐性+15<br>";
	} else if (kago > 3) {
		document.getElementById("setBonus").innerHTML += "全狀態異常耐性+10<br>";
		document.getElementById("setBonusEm").innerHTML += "全狀態異常耐性+10<br>";
	} else if (kago > 1) {
		document.getElementById("setBonus").innerHTML += "全狀態異常耐性+5<br>";
		document.getElementById("setBonusEm").innerHTML += "全狀態異常耐性+5<br>";
	}
	// 宝石
	var houseki = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "06")
			houseki++;
	}
	if (houseki > 3) {
		document.getElementById("setBonus").innerHTML += "起始MP+10<br>";
		document.getElementById("setBonusEm").innerHTML += "起始MP+10<br>";
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
	// 技巧
	var gikou = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "09")
			gikou++;
	}
	if (gikou > 5) {
		document.getElementById("setBonus").innerHTML += "命中+30<br>";
		document.getElementById("setBonusEm").innerHTML += "命中+30<br>";
	} else if (gikou > 3) {
		document.getElementById("setBonus").innerHTML += "命中+20<br>";
		document.getElementById("setBonusEm").innerHTML += "命中+20<br>";
	} else if (gikou > 1) {
		document.getElementById("setBonus").innerHTML += "命中+10<br>";
		document.getElementById("setBonusEm").innerHTML += "命中+10<br>";
	}
	//疾駆
	var genzou = 0;
	for (var i = 0; i < setCount.length; ++i) {
		if (setCount[i] == "10")
			genzou++;
	}
	if (genzou > 3) {
		document.getElementById("setBonus").innerHTML += "回避+10";
		document.getElementById("setBonusEm").innerHTML += "回避+10";
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

	function sumUpGivenStat(slot, min, max) {
		var statGiven = "stat" + slot + "Given";
		if (document.getElementById(statGiven).value == 0) {
			console.log("No given basic stat for rune" + slot + ".")
			document.getElementById("stat" + slot + "G").innerHTML = "隨機";
			switch (slot) {
				case 1:
				case 2:
				case 4:
				case 5:
					randomStat("A", document.getElementById("rank" + slot).value, slot);
					break;
				case 3:
					randomStat("B", document.getElementById("rank" + slot).value, slot);
					break;
				case 6:
					randomStat("C", document.getElementById("rank" + slot).value, slot);
					break;
			}
		} else if (document.getElementById(statGiven).value >= min && document.getElementById(statGiven).value <= max) {
			statGivenSum += document.getElementById("stat" + slot + "Given").value;
			document.getElementById("stat" + slot + "Em").innerHTML = document.getElementById("stat" + slot + "Given").value
			document.getElementById("stat" + slot + "G").innerHTML = document.getElementById("stat" + slot + "Given").value
			document.getElementById("statGiven").style.display = "table-row";
		} else {
			console.log("Given basic stat for rune" + slot + " is " + document.getElementById("stat" + slot + "Given").value + "; should be within " + min + " and " + max + ".");
			alert("Given data is corrupted - rune" + slot + "$基礎屬性\nProceeding while ignoring the given data.");
			document.getElementById("stat" + slot + "G").innerHTML = "隨機";
			switch (slot) {
				case 1:
				case 2:
				case 4:
				case 5:
					randomStat("A", document.getElementById("rank" + slot).value, slot);
					break;
				case 3:
					randomStat("B", document.getElementById("rank" + slot).value, slot);
					break;
				case 6:
					randomStat("C", document.getElementById("rank" + slot).value, slot);
					break;
			}
		}
	}

	var statGivenSum = 0;
	for (var slot = 1; slot <= 6; slot++) {
		switch (slot) {
			case 1:
			case 2:
			case 4:
			case 5:
				switch (document.getElementById("rank" + slot).value) {
					case "ssr":
						sumUpGivenStat(slot, 76, 100);
						break;
					case "sr":
						sumUpGivenStat(slot, 31, 55);
						break;
					case "r":
						sumUpGivenStat(slot, 1, 25);
						break;
				}
				break;
			case 3:
				switch (document.getElementById("rank" + slot).value) {
					case "ssr":
						sumUpGivenStat(slot, 501, 700);
						break;
					case "sr":
						sumUpGivenStat(slot, 221, 420);
						break;
					case "r":
						sumUpGivenStat(slot, 101, 200);
						break;
				}
				break;
			case 6:
				switch (document.getElementById("rank" + slot).value) {
					case "ssr":
						sumUpGivenStat(slot, 8, 10);
						break;
					case "sr":
						sumUpGivenStat(slot, 4, 6);
						break;
					case "r":
						sumUpGivenStat(slot, 1, 3);
						break;
				}
				break;
		}
	}
	if (statGivenSum > 0) {
		console.log("Given basic stat available. Visualizing the corresponding table row.")
		document.getElementById("statGiven").style.display = "table-row";
	} else {
		console.log("No given basic stat for the rune set.")
	}
	refreshStats();

	/* Convert input values to JSON and paste to textarea#jsonOutput */
	var data = createJSON();
	document.getElementById("jsonOutput").value = JSON.stringify(data);
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

function evoStat(slot, evoStatEmId, evoStatIntEmId) {
	// slot, tdId(#evoStat), tdId(#evoStatIntEm)
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
					document.getElementById(evoStatEmId).innerHTML = "憤怒耐性";
					break;
				case 7:
					document.getElementById(evoStatEmId).innerHTML = "時緩耐性";
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
					document.getElementById(evoStatEmId).innerHTML = "暗闇耐性";
					break;
				case 2:
					document.getElementById(evoStatEmId).innerHTML = "石化耐性";
					break;
				case 3:
					document.getElementById(evoStatEmId).innerHTML = "沈默耐性";
					break;
				case 4:
					document.getElementById(evoStatEmId).innerHTML = "移動禁止耐性";
					break;
				case 5:
					document.getElementById(evoStatEmId).innerHTML = "攻擊禁止耐性";
					break;
				case 6:
					document.getElementById(evoStatEmId).innerHTML = "死之宣告耐性";
					break;
				case 7:
					document.getElementById(evoStatEmId).innerHTML = "時停耐性";
					break;
				case 8:
					document.getElementById(evoStatEmId).innerHTML = "回復無效耐性";
					break;
				case 9:
					document.getElementById(evoStatEmId).innerHTML = "補助行動禁止耐性";
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

function gauge(slot) {
	console.log("Gauging rune" + slot + ".");
	var baseRate = parseInt(document.getElementById("enRate" + slot).innerHTML);
	if (baseRate == "N/A") {
		console.log("Invalid base rate.");
	} else {
		var rank = document.getElementById("rank" + slot).value;
		switch (rank) {
			case "ssr":
				var q = 5;
				break;
			case "sr":
				var q = 4;
				break;
			case "r":
				var q = 3;
				break;
		}
		if (document.getElementById("enRate" + slot).innerHTML != "100%") {
			var btnGauge = document.getElementsByClassName("useGauge" + q);
			for (i = 0; i < btnGauge.length; i++) {
				btnGauge[i].disabled = true;
				document.getElementById("enRate" + slot).innerHTML = "100%";
				document.getElementById("gauge" + q).innerHTML = (baseRate + "%");
				console.log("Enhance success rate for rune" + slot + " has been forced to 100%. New gauge(" + q + ") is " + baseRate + "%.");
			}
		} else {
			console.log("Base rate is already 100%.")
		}
	}
}

function enhance(slot, rank) {
	enRate = "enRate" + slot;
	useGauge = "useGauge" + slot;
	gauging = "gauging" + slot;
	lv = "lv" + slot;
	console.log("Enhancing rune" + slot + ".");
	var roll = randomInt(1, 100);
	document.getElementById("rolled").innerHTML = (roll + " / 100");
	var baseRate = parseInt(document.getElementById(enRate).innerHTML);
	console.log("Base rate is " + baseRate + ".")

	if (roll > (100 - baseRate)) {
		document.getElementById("range").innerHTML = "強化成功";
		return true;
	} else {
		var failedBonus = 0;
		var evo = document.getElementById(lv).innerHTML.substring(2, 3);
		switch (rank) {
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
				gaugeOld = "gauge5";
				useGauge = "useGauge5";
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
				gaugeOld = "gauge4";
				useGauge = "useGauge4";
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
				gaugeOld = "gauge3";
				useGauge = "useGauge3";
				break;
			default:
				console.log("Error in enhance(" + slot + ", " + rank + "), please check.");
		}
		console.log("Gauge increased by " + failedBonus + "%, cap at 100%.");
		gaugeNew = Math.min(100, parseInt(document.getElementById(gaugeOld).innerHTML) + parseInt(failedBonus));
		if (gaugeNew == 100) {
			console.log("Gauge has been filled.");
			var btnGauge = document.getElementsByClassName(useGauge);
			for (i = 0; i < btnGauge.length; i++) {
				btnGauge[i].disabled = false;
			}
		}
		document.getElementById(gaugeOld).innerHTML = (gaugeNew + "%");
		document.getElementById("range").innerHTML = "強化失敗";
		return false;
	}
}

function upgrade(set, slot) {
	var statEnId = document.getElementById("statEn" + slot);
	var level = document.getElementById("lv" + slot);
	var rank = document.getElementById("rank" + slot).value;
	var enRate = "enRate" + slot;
	var useGauge = "useGauge" + slot;
	var btn = document.getElementById("en" + slot);
	var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
	var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
	var stoneGreen = parseInt(document.getElementById("stoneGreen").innerHTML.replace(/\,/g, ''));
	var stoneBlue = parseInt(document.getElementById("stoneBlue").innerHTML.replace(/\,/g, ''));
	var stoneYellow = parseInt(document.getElementById("stoneYellow").innerHTML.replace(/\,/g, ''));
	var stoneRed = parseInt(document.getElementById("stoneRed").innerHTML.replace(/\,/g, ''));
	var roll = randomInt(1, 100);
	document.getElementById("rolled").innerHTML = (roll + " / 100");
	var output = statEnId.innerHTML;
	var cost = costGreen = costBlue = costYellow = costRed = 0

	switch (level.innerHTML) {
		case "覺醒0 強化0":
			switch (rank) {
				case "ssr":
					cost = 90000;
					costGreen = 5;
					break;
				case "sr":
					cost = 60000;
					costGreen = 4;
					break;
				case "r":
					cost = 30000;
					costGreen = 3;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒0 強化1":
			switch (rank) {
				case "ssr":
					cost = 180000;
					costGreen = 5;
					break;
				case "sr":
					cost = 120000;
					costGreen = 4;
					break;
				case "r":
					cost = 60000;
					costGreen = 3;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒0 強化2":
			switch (rank) {
				case "ssr":
					cost = 270000;
					costGreen = 5;
					break;
				case "sr":
					cost = 180000;
					costGreen = 4;
					break;
				case "r":
					cost = 90000;
					costGreen = 3;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				// document.getElementById(useGauge).style.display = "none";
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒0 強化3": //覺醒
			switch (rank) {
				case "ssr":
					cost = 1500000;
					costRed = 1;
					break;
				case "sr":
					cost = 1000000;
					costYellow = 1;
					break;
				case "r":
					cost = 500000;
					costBlue = 1;
					break;
			}
			level.innerHTML = "覺醒1 強化0";
			btn.innerHTML = "強化";
			btn.className = "en";
			// document.getElementById(useGauge).style.display = "inline-block";
			document.getElementById(enRate).innerHTML = "100%";
			evoStat(slot, "evoStatEm" + "1" + slot, "evoStatIntEm" + "1" + slot);
			break;
		case "覺醒1 強化0":
			switch (rank) {
				case "ssr":
					cost = 600000;
					costGreen = 8;
					break;
				case "sr":
					cost = 400000;
					costGreen = 6;
					break;
				case "r":
					cost = 200000;
					costGreen = 5;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒1 強化1":
			switch (rank) {
				case "ssr":
					cost = 750000;
					costGreen = 8;
					break;
				case "sr":
					cost = 500000;
					costGreen = 6;
					break;
				case "r":
					cost = 250000;
					costGreen = 5;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒1 強化2":
			switch (rank) {
				case "ssr":
					cost = 900000;
					costGreen = 8;
					break;
				case "sr":
					cost = 600000;
					costGreen = 6;
					break;
				case "r":
					cost = 300000;
					costGreen = 5;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				// document.getElementById(useGauge).style.display = "none";
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒1 強化3": //覺醒
			switch (rank) {
				case "ssr":
					cost = 3000000;
					costRed = 3;
					break;
				case "sr":
					cost = 2000000;
					costYellow = 3;
					break;
				case "r":
					cost = 1000000;
					costBlue = 3;
					break;
			}
			level.innerHTML = "覺醒2 強化0";
			btn.innerHTML = "強化";
			// document.getElementById(useGauge).style.display = "inline-block";
			document.getElementById(enRate).innerHTML = "100%";
			btn.className = "en";
			evoStat(slot, "evoStatEm" + "2" + slot, "evoStatIntEm" + "2" + slot);
			break;
		case "覺醒2 強化0":
			switch (rank) {
				case "ssr":
					cost = 2100000;
					costGreen = 33;
					break;
				case "sr":
					cost = 1400000;
					costGreen = 26;
					break;
				case "r":
					cost = 700000;
					costGreen = 20;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒2 強化1":
			switch (rank) {
				case "ssr":
					cost = 2400000;
					costGreen = 33;
					break;
				case "sr":
					cost = 1600000;
					costGreen = 26;
					break;
				case "r":
					cost = 800000;
					costGreen = 20;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒2 強化2":
			switch (rank) {
				case "ssr":
					cost = 2700000;
					costGreen = 33;
					break;
				case "sr":
					cost = 1800000;
					costGreen = 26;
					break;
				case "r":
					cost = 900000;
					costGreen = 20;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				// document.getElementById(useGauge).style.display = "none";
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒2 強化3": //覺醒
			switch (rank) {
				case "ssr":
					cost = 4500000;
					costRed = 5;
					break;
				case "sr":
					cost = 3000000;
					costYellow = 5;
					break;
				case "r":
					cost = 1500000;
					costBlue = 5;
					break;
			}
			level.innerHTML = "覺醒3 強化0";
			btn.innerHTML = "強化";
			// document.getElementById(useGauge).style.display = "inline-block";
			document.getElementById(enRate).innerHTML = "100%";
			btn.className = "en";
			evoStat(slot, "evoStatEm" + "3" + slot, "evoStatIntEm" + "3" + slot);
			break;
		case "覺醒3 強化0":
			switch (rank) {
				case "ssr":
					cost = 9000000;
					costGreen = 150;
					break;
				case "sr":
					cost = 6000000;
					costGreen = 120;
					break;
				case "r":
					cost = 3000000;
					costGreen = 90;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒3 強化1":
			switch (rank) {
				case "ssr":
					cost = 9900000;
					costGreen = 150;
					break;
				case "sr":
					cost = 6600000;
					costGreen = 120;
					break;
				case "r":
					cost = 3300000;
					costGreen = 90;
					break;
			}
			if (enhance(slot, rank) == true) {
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
				document.getElementById(enRate).innerHTML = "100%";
			}
			break;
		case "覺醒3 強化2":
			switch (rank) {
				case "ssr":
					cost = 10800000;
					costGreen = 150;
					break;
				case "sr":
					cost = 7200000;
					costGreen = 120;
					break;
				case "r":
					cost = 3600000;
					costGreen = 90;
					break;
			}
			if (enhance(slot, rank) == true) {
				switch (set) {
					case "A":
						output = 25;
						break;
					case "B":
						output = 120;
						break;
					case "C":
						switch (rank) {
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
				// document.getElementById(useGauge).style.display = "none";
				document.getElementById(enRate).innerHTML = "N/A";
			}
			break;
		default:
			console.log("Error in upgrade(" + set + ", " + slot + "), please check.");
	}
	statEnId.innerHTML = output
	document.getElementById("zeni").innerHTML = Intl.NumberFormat('en-US').format(zeni + cost);
	document.getElementById("stoneGreen").innerHTML = Intl.NumberFormat('en-US').format(stoneGreen + costGreen);
	document.getElementById("stoneBlue").innerHTML = Intl.NumberFormat('en-US').format(stoneBlue + costBlue);
	document.getElementById("stoneYellow").innerHTML = Intl.NumberFormat('en-US').format(stoneYellow + costYellow);
	document.getElementById("stoneRed").innerHTML = Intl.NumberFormat('en-US').format(stoneRed + costRed);
	refreshStats();
}

function rerollBasicStat(set, slot) {
	var rank = document.getElementById("rank" + slot).value
	randomStat(set, rank, slot);
	refreshStats();

	var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
	var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
	switch (rank) {
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
		evoStat(slot, evoStatEmId, evoStatIntEmId);
		refreshStats();

		var rank = document.getElementById("rank" + slot).value;
		var zeni = parseInt(document.getElementById("zeni").innerHTML.replace(/\,/g, ''));
		var gem = parseInt(document.getElementById("gem").innerHTML.replace(/\,/g, ''));
		switch (rank) {
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

function enhanceEvo(row, slot) {
	var evoStatEmId = "evoStatEm" + row + slot;
	var evoStatIntEmId = "evoStatIntEm" + row + slot;
	var evoStatSet;
	if (document.getElementById(evoStatEmId).innerHTML == "N/A") {
		console.log("Invalid level");
	} else {
		function hammer() {
			var p = parseInt(randomInt(1, 100));
			document.getElementById("rolled").innerHTML = (p + " / 100");
			if (p > 0) {
				document.getElementById(evoStatIntEmId).innerHTML = parseInt(document.getElementById(evoStatIntEmId).innerHTML) + 1;
				document.getElementById("range").innerHTML = "效果強化成功";
			} else {
				document.getElementById("range").innerHTML = "效果強化失敗";
			}
			var rank = document.getElementById("rank" + slot).value;
			var hammer = parseInt(document.getElementById("hammer").innerHTML.replace(/\,/g, ''));
			switch (rank) {
				case "ssr":
					document.getElementById("hammer").innerHTML = Intl.NumberFormat('en-US').format(hammer + 15);
					break;
				case "sr":
					document.getElementById("hammer").innerHTML = Intl.NumberFormat('en-US').format(hammer + 9);
					break;
				case "r":
					document.getElementById("hammer").innerHTML = Intl.NumberFormat('en-US').format(hammer + 3);
					break;
			}
		}
		if (document.getElementById(evoStatEmId).innerHTML == "根性") {
			if (document.getElementById(evoStatIntEmId).innerHTML = 3) {
				console.log("Already maximum (set C)");
				document.getElementById("range").innerHTML = "已達到最大值";
			} else {
				hammer();
			}
		} else {
			switch (document.getElementById(evoStatEmId).innerHTML) {
				case "斬擊攻擊":
				case "打擊攻擊":
				case "刺突攻擊":
				case "射撃攻擊":
				case "魔法攻擊":
				case "跳躍攻擊":
				case "MP獲得量":
				case "治癒力":
				case "暴擊率":
					if (document.getElementById(evoStatIntEmId).innerHTML == 5) {
						console.log("Already maximum (set A)");
						document.getElementById("range").innerHTML = "已達到最大值";
					} else {
						hammer();
					}
					break;
				default:
					if (document.getElementById(evoStatIntEmId).innerHTML == 10) {
						console.log("Already maximum (set B)");
						document.getElementById("range").innerHTML = "已達到最大值";
					} else {
						hammer();
					}
			}
		}
		refreshStats();
	}
}
