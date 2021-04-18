function contains(selector, text) {
	var elements = document.querySelectorAll(selector);
	return Array.prototype.filter.call(elements, function(element){
		return RegExp(text).test(element.textContent);
	});
}

function trContains(elements, string) {
	return Array.prototype.filter.call(elements, function(tr){
		return tr.innerHTML.indexOf(string) > 0;
  });
}

function trNotContains(elements, string) {
	return Array.prototype.filter.call(elements, function (tr) {
		return tr.textContent.indexOf(string) == -1;
	});
}

function trIsNotHidden(elements) {
	return Array.prototype.filter.call(elements, function (tr) {
		return tr.style.display.indexOf('none') == -1;
	});
}

function chooseAllExtra() {
	var extra = document.querySelectorAll('[id^=ex]');
	for (i = 0; i < extra.length; i++) {
		extra[i].checked = true;
	}
	score();
}

function clearExtra() {
	var extra = document.querySelectorAll('[id^=ex]');
	for (i = 0; i < extra.length; i++) {
		extra[i].checked = false;
	}
	score();
}

function chooseTypeExtra() {
	clearExtra();
	var extra = document.querySelectorAll('[id^=ex]');
	for (i = 0; i < 6; i++) {
		extra[i].checked = true;
	}
	score();
}

function showNote() {
	var x = document.getElementById('history');
	if (x.style.display == 'none') {
		x.style.display = 'table-row-group';
		document.getElementById('showBtn').innerHTML = 'Hide update history';
	} else {
		x.style.display = 'none';
		document.getElementById('showBtn').innerHTML = 'Show update history';
	}
}

function hideGlobal() {
	var globalOriginal = trContains(document.querySelectorAll("tr.mmt"), "TS_GL_");
	for (i = 0; i < globalOriginal.length; i++) {
		globalOriginal[i].style.display = "none";
	}
}

function checkGroup() {
	document.getElementById('d5').selectedIndex = 0;
	refreshMmt();
	for (i = 0; i < document.getElementById("d5").options.length; i++) {
		switch (i) {
			case 0:
				var mmt = trIsNotHidden(document.querySelectorAll('tr.mmt')).length;
				break;
			case 1:
				var mmt = trIsNotHidden(document.querySelectorAll('tr.mmt.groupless')).length;
				break;
			default:
				var groupSelector = document.getElementById("d5").options[i].value;
				var mmt = trContains(trIsNotHidden(document.querySelectorAll('tr.mmt')), groupSelector).length;
		}
		var gNum = "g" + i;
		document.getElementById(gNum).innerText = document.getElementById(gNum).innerText.split(" [")[0] + " [" + mmt + "]";
		if (mmt == 0) {
			document.getElementById(gNum).style.color = "lightgrey";
		} else {
			document.getElementById(gNum).style.color = "black";
		}
	}
}

function checkFilter() {
	mode = document.getElementById("g" + document.getElementById("d5").options.selectedIndex).style.color;
	index = document.getElementById("d5").options.selectedIndex;
	if (mode == "lightgrey") {
		document.getElementById('d4').selectedIndex = 0;
		console.log('Automation: [d4]Mementos from All Regions are shown.');
		document.getElementById('d5').selectedIndex = 0;
		for (i = 1; i < document.getElementById("d4").options.length; i++) {
			var rNum = "r" + i;
			document.getElementById(rNum).style.color = "black";
		}
		refreshMmt();
		checkGroup();
		document.getElementById('d5').selectedIndex = index;
		refreshMmt();
	}
	var url = location.href;				//Save down the URL without hash.
    location.href = "#mementos";			//Go to the target element.
    history.replaceState(null,null,url);	//Don't like hashes. Changing it back.
}



function refreshMmt() {
	// Decide what info to show
	var optInfo = [
		document.querySelectorAll('[headers = "HP"]'),
		document.querySelectorAll('[headers = "pdef"]'),
		document.querySelectorAll('[headers = "mdef"]'),
		document.querySelectorAll('[headers = "dex"]'),
		document.querySelectorAll('[headers = "agi"]'),
		document.querySelectorAll('[headers = "luck"]'),
		document.querySelectorAll('[headers = "others"]'),
		];
	if (document.querySelector('input[name = "optInfo"]:checked').value == "hide") {
		// console.log("[o0]Secondary info has been hidden.");
		for (i = 0; i < optInfo.length; i++) {
			for (j = 0; j < optInfo[i].length; j++) {
				optInfo[i][j].style.display = "none";
			}
		}
	} else if (document.querySelector('input[name = "optInfo"]:checked').value == "show") {
		// console.log("[o0]Displaying all info.");
		for (i = 0; i < optInfo.length; i++) {
			for (j = 0; j < optInfo[i].length; j++) {
				optInfo[i][j].style.display = "table-cell";
			}
		}
	}
	
	// Decide display style (text or logo)
	var originName = document.getElementsByClassName('originName');
	var originLogo = document.getElementsByClassName('originLogo');
	if (document.querySelector('input[name = "optOrigin"]:checked').value == "text") {
		// console.log("[o1]Displaying origin by text.");
		for (i = 0; i < originName.length; i++) {
			originName[i].style.display = 'inline';
			originLogo[i].style.display = 'none';
		}
	} else if (document.querySelector('input[name = "optOrigin"]:checked').value == "logo") {
		// console.log("[o1]Displaying origin by logo.");
		for (i = 0; i < originName.length; i++) {
			originName[i].style.display = 'none';
			originLogo[i].style.display = 'inline';
		}
	}
	
	var groupName = document.getElementsByClassName('groupName');
	var groupLogo = document.getElementsByClassName('groupLogo');
	if (document.querySelector('input[name = "optGroup"]:checked').value == "text") {
		// console.log("[o2]Displaying group by text.");
		for (i = 0; i < groupName.length; i++) {
			groupName[i].style.display = 'inline';
			groupLogo[i].style.display = 'none';
		}
	} else if (document.querySelector('input[name = "optGroup"]:checked').value == "logo") {
		// console.log("[o2]Displaying group by logo.");
		for (i = 0; i < groupName.length; i++) {
			groupName[i].style.display = 'none';
			groupLogo[i].style.display = 'inline';
		}
	}
	
	// Show or hide all memento rows according to normal pool option
	var x = document.getElementsByClassName('mmt');
	if (document.getElementById('d0').checked === true) {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = 'table-row';
		}
		// console.log("[d0]普池 mementos are shown.")
	} else {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = 'none';
		}
		// console.log("[d0]普池 mementos are hidden.")
	}

	// Show rows according to event / limited options
	for (i = 1; i <= 2; i++) {
		var y = document.getElementById('d' + i);
		var z = document.getElementsByClassName(y.value);
		if (y.checked === true) {
			// console.log('[d' + i + ']' + document.getElementById('labelD' + i).innerText + ' mementos are shown.');
			for (j = 0; j < z.length; j++) {
				z[j].style.display = 'table-row';
			}
		} else {
			// console.log('[d' + i + ']' + document.getElementById('labelD' + i).innerText + ' mementos are hidden.');
			for (j = 0; j < z.length; j++) {
				z[j].style.display = 'none';
			}
		}
	}
	
	// Show rows based on origin option
	var originSelector = document.getElementById("d4").value;
	if (originSelector == "all") {
		var mmt = [];
		// console.log('[d4]Mementos from all regions are shown.');
	} else {
		var mmt = trNotContains(document.querySelectorAll('tr.mmt'), originSelector);
		// console.log('[d5]Only ' + originSelector + ' mementos are shown.');
	}
	for (j = 0; j < mmt.length; j++) {
		mmt[j].style.display = 'none';
	}
	
	// Show rows based on group option
	var groupSelector = document.getElementById("d5").value;
	switch (groupSelector) {
		case "all":
			var mmt = [];
			// console.log('[d5]No group restriction is imposed.');
			break;
		case "groupless":
			mmt = document.querySelectorAll('tr.mmt:not(.groupless)');
			// console.log('[d5]Only groupless mementos are shown.');
			if (document.getElementById('d3').checked === false) {
				document.getElementById('d3').checked = true;
				console.log('Automation: [d3]顯示無團隊 changed to true.');
			}
			break;
		default:
			mmt = trNotContains(document.querySelectorAll('tr.mmt'), groupSelector);
			// console.log('[d5]Only ' + groupSelector + ' mementos are shown.');
	}
	
	for (j = 0; j < mmt.length; j++) {
		mmt[j].style.display = "none";
	}

	// Arrange groupless mementos according to display option
	var groupless = document.getElementsByClassName('groupless');	
	if (document.getElementById('d3').checked === true) {
		// console.log('[d3]無團隊 mementos are shown.')
	} else {
		// console.log('[d3]無團隊 mementos are hidden.')
		for (j = 0; j < groupless.length; j++) {
			groupless[j].style.display = 'none';
		}
	}

	$('tr:visible').removeClass('odd').filter(':odd').addClass('odd');
	// Hide Global Originals for Chinese page
	if (window.location.href.indexOf('_en') == -1) {
		hideGlobal();
		// console.log("Global Originals mementos have been hidden.");
	}
	
	// Show the number of filtered result
	document.getElementById("mmtCount").innerHTML = trIsNotHidden(document.querySelectorAll('tr.mmt')).length;
	
	// console.log("=====End of refreshMmt=====");
}

function sortTableByString(n) {
	var table,
		rows,
		switching,
		i,
		x,
		y,
		shouldSwitch,
		dir,
		switchcount = 0;
	table = document.getElementById('mementos');
	switching = true;
	// Set the sorting direction to descending:
	dir = 'desc';

	/*Make a loop that will continue until no switching has been done:*/
	while (switching) {
		//start by saying: no switching is done:
		switching = false;
		rows = table.rows;

		/*Loop through all table rows (except the first, which contains table headers):*/
		for (i = 1; i < (rows.length - 1); i++) {
			//start by saying there should be no switching:
			shouldSwitch = false;
			/*Get the two elements you want to compare, one from current row and one from the next:*/
			x = rows[i].getElementsByTagName('TD')[n];
			y = rows[i + 1].getElementsByTagName('TD')[n];

			/*check if the two rows should switch place, based on the direction, asc or desc:*/
			if (dir == 'asc') {
				if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					break;
				}
			} else if (dir == 'desc') {
				if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					break;
				}
			}
		}

		if (shouldSwitch) {
			/*If a switch has been marked, make the switch and mark that a switch has been done:*/
			rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			switching = true;
			//Each time a switch is done, increase this count by 1:
			switchcount++;
		} else {

			/*If no switching has been done AND the direction is 'desc', set the direction to 'asc' and run the while loop again.*/
			if (switchcount == 0 && dir == 'desc') {
				dir = 'asc';
				switching = true;
			}
		}
	}
	refreshMmt();
}

function sortTableByNumber(n) {
	var table,
		rows,
		switching,
		i,
		x,
		y,
		shouldSwitch,
		dir,
		switchcount = 0;
	table = document.getElementById('mementos');
	switching = true;
	//Set the sorting direction to descending:
	dir = 'desc';

	/*Make a loop that will continue until no switching has been done:*/
	while (switching) {
		//start by saying: no switching is done:
		switching = false;
		rows = table.rows;

		/*Loop through all table rows (except the first, which contains table headers):*/
		for (i = 1; i < (rows.length - 1); i++) {
			//start by saying there should be no switching:
			shouldSwitch = false;
			/*Get the two elements you want to compare, one from current row and one from the next:*/
			x = rows[i].getElementsByTagName('TD')[n];
			y = rows[i + 1].getElementsByTagName('TD')[n];

			/*check if the two rows should switch place, based on the direction, asc or desc:*/
			if (dir == 'asc') {
				if (Number(x.innerHTML) > Number(y.innerHTML)) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					break;
				}
			} else if (dir == 'desc') {
				if (Number(x.innerHTML) < Number(y.innerHTML)) {
					//if so, mark as a switch and break the loop:
					shouldSwitch = true;
					break;
				}
			}
		}

		if (shouldSwitch) {
			/*If a switch has been marked, make the switch and mark that a switch has been done:*/
			rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
			switching = true;
			//Each time a switch is done, increase this count by 1:
			switchcount++;
		} else {

			/*If no switching has been done AND the direction is 'desc', set the direction to 'asc' and run the while loop again.*/
			if (switchcount == 0 && dir == 'desc') {
				dir = 'asc';
				switching = true;
			}
		}
	}
	refreshMmt();
}

function replaceKeyword(selector, oldStr, newStr) {
	var str = contains(selector, oldStr);
	for (i = 0; i < str.length; i++) {
		str[i].innerHTML = str[i].innerHTML.replace(oldStr, newStr);
	}
}

function translate() {
	// show Global Origins in selection list
	document.getElementById("g29").style.display = "";
	
	// translate headers
	var headers = document.getElementsByTagName('th');
	headers[0].innerText = "Icon";
	headers[1].innerText = "Rank";
	headers[3].innerText = "R";
	headers[4].innerText = "Origin";
	headers[5].innerText = "Group";
	headers[6].innerText = "Score";
	headers[7].innerText = "HP";
	headers[8].innerText = "PAtk";
	headers[9].innerText = "MAtk";
	headers[10].innerText = "PDef";
	headers[11].innerText = "MDef";
	headers[12].innerText = "Dex";
	headers[13].innerText = "Agi";
	headers[14].innerText = "Luc";
	headers[15].innerText = "Atk.Type";
	headers[16].innerText = "Bonus";
	headers[17].innerText = "Vs";
	headers[18].innerText = "Bonus";
	headers[19].innerText = "Misc";
	headers[20].innerText = "Env";
	headers[21].innerText = "Slo";
	headers[22].innerText = "Lus";
	headers[23].innerText = "Glu";
	headers[24].innerText = "Wra";
	headers[25].innerText = "Gre";
	headers[26].innerText = "Pri";
	
	// translate keywords in mmtList
	replaceKeyword("span.event", "活動", "E");
	replaceKeyword("span.limited", "限定", "L");
	replaceKeyword("td[headers=aType]", "斬撃", "Slash");
	replaceKeyword("td[headers=aType]", "刺突", "Pierce");
	replaceKeyword("td[headers=aType]", "打撃", "Blow");
	replaceKeyword("td[headers=aType]", "射撃", "Missle");
	replaceKeyword("td[headers=aType]", "魔法", "Magic");
	replaceKeyword("td[headers=aType]", "無区分", "Non-type");
	replaceKeyword("td[headers=special]", "反撃", "Counter");
	replaceKeyword("td[headers=special]", "火属性", "Fire");
	replaceKeyword("td[headers=special]", "雷属性", "Thunder");
	replaceKeyword("td[headers=special]", "風属性", "Wind");
	replaceKeyword("td[headers=special]", "闇属性", "Dark");
	replaceKeyword("td[headers=special]", "単体", "Single");
	replaceKeyword("td[headers=special]", "範囲", "Area");
	replaceKeyword("td[headers=special]", "異族", "Eldritch");
	replaceKeyword("td[headers=special]", "バジュラ", "Vajra");
	replaceKeyword("td[headers=special]", "魔動人形", "Demon Golem");
	replaceKeyword("td[headers=special]", "下位魔神", "Sub-Demon");
	replaceKeyword("td[headers=special]", "巨体", "Gigantic");
	replaceKeyword("td[headers=special]", "人", "Human");
	replaceKeyword("td[headers=others]", "MP上限", "MaxJewel");
	replaceKeyword("td[headers=others]", "MP回復", "JewelGain");
	replaceKeyword("td[headers=others]", "命中率", "Hit");
	replaceKeyword("td[headers=others]", "斬撃回避率", "SlashEvasion");
	replaceKeyword("td[headers=others]", "射撃回避率", "MissleEvasion");
	replaceKeyword("td[headers=others]", "魔法回避率", "MagicEvasion");
	replaceKeyword("td[headers=others]", "回避率", "Evasion");
	replaceKeyword("td[headers=others]", "暴擊率", "CritRate");
	replaceKeyword("td[headers=others]", "詠唱時間", "Casting");
	replaceKeyword("td[headers=others]", "水属性耐性", "WaterRes");
	replaceKeyword("td[headers=others]", "火属性耐性", "FireRes");
	replaceKeyword("td[headers=others]", "風属性耐性", "WindRes");
	replaceKeyword("td[headers=others]", "光属性耐性", "LightRes");
	replaceKeyword("td[headers=others]", "闇属性耐性", "DarkRes");
	replaceKeyword("td[headers=others]", "斬撃耐性", "SlashRes");
	replaceKeyword("td[headers=others]", "刺突耐性", "PierceRes");
	replaceKeyword("td[headers=others]", "射撃耐性", "MissleRes");
	replaceKeyword("td[headers=others]", "単体耐性", "SingleRes");
	replaceKeyword("td[headers=others]", "範囲耐性", "AreaRes");
	replaceKeyword("td[headers=others]", "治癒力", "Healing");
	replaceKeyword("td[headers=others]", "魅了", "CharmRes");
	replaceKeyword("td[headers=others]", "沈黙", "SilenceRes");
	replaceKeyword("td[headers=others]", "対巨体防御", "GiganticRes");
	replaceKeyword("td[headers=others]", "会心", "Crit");
}

