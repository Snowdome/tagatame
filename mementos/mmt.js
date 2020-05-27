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

function refreshMmt() {
	// Show or hide all memento rows according to normal pool option
	var x = document.getElementsByClassName('mmt');
	if (document.getElementById('d0').checked == true) {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = 'table-row';
		}
	} else {
		for (i = 0; i < x.length; i++) {
			x[i].style.display = 'none';
		}
	}
	
	// then decide what info to show
	var secInfo = [
		document.querySelectorAll('[headers = "HP"]'),
		document.querySelectorAll('[headers = "pdef"]'),
		document.querySelectorAll('[headers = "mdef"]'),
		document.querySelectorAll('[headers = "dex"]'),
		document.querySelectorAll('[headers = "agi"]'),
		document.querySelectorAll('[headers = "luck"]'),
		document.querySelectorAll('[headers = "others"]'),
		];
	if (document.querySelector('input[name = "secInfo"]:checked').value == "hide") {
		console.log("Secondary info has been hidden.");
		for (i = 0; i < secInfo.length; i++) {
			for (j = 0; j < secInfo[i].length; j++) {
				secInfo[i][j].style.display = "none";
			}
		}
	} else if (document.querySelector('input[name = "secInfo"]:checked').value == "show") {
		console.log("Displaying all info.");
		for (i = 0; i < secInfo.length; i++) {
			for (j = 0; j < secInfo[i].length; j++) {
				secInfo[i][j].style.display = "table-cell";
			}
		}
	}
	
	// then decide display style (text or logo)
	var originName = document.getElementsByClassName('originName');
	var originLogo = document.getElementsByClassName('originLogo');
	if (document.querySelector('input[name = "optOrigin"]:checked').value == "text") {
		console.log("Displaying origin by text.");
		for (i = 0; i < originName.length; i++) {
			originName[i].style.display = 'inline';
			originLogo[i].style.display = 'none';
		}
	} else if (document.querySelector('input[name = "optOrigin"]:checked').value == "logo") {
		console.log("Displaying origin by logo.");
		for (i = 0; i < originName.length; i++) {
			originName[i].style.display = 'none';
			originLogo[i].style.display = 'inline';
		}
	}
	
	var groupName = document.getElementsByClassName('groupName');
	var groupLogo = document.getElementsByClassName('groupLogo');
	if (document.querySelector('input[name = "optGroup"]:checked').value == "text") {
		console.log("Displaying group by text.");
		for (i = 0; i < groupName.length; i++) {
			groupName[i].style.display = 'inline';
			groupLogo[i].style.display = 'none';
		}
	} else if (document.querySelector('input[name = "optGroup"]:checked').value == "logo") {
		console.log("Displaying group by logo.");
		for (i = 0; i < groupName.length; i++) {
			groupName[i].style.display = 'none';
			groupLogo[i].style.display = 'inline';
		}
	}

	// then show rows per event / limited options
	for (i = 1; i <= 2; i++) {
		var y = document.getElementById('d' + i);
		var z = document.getElementsByClassName(y.value);
		if (y.checked == true) {
			console.log('Option [d' + i + ']' + document.getElementById('labelD' + i).innerText + ' is shown.')
			for (j = 0; j < z.length; j++) {
				z[j].style.display = 'table-row';
			}
		} else {
			console.log('Option [d' + i + ']' + document.getElementById('labelD' + i).innerText + ' is hidden.')
			for (j = 0; j < z.length; j++) {
				z[j].style.display = 'none';
			}
		}
	}
		
	// finally hide rows if show groupless is not checked
	var groupless = document.getElementsByClassName('groupless');
	if (document.getElementById('d3').checked == true) {
		console.log('Option [d3]' + document.getElementById('labelD' + i).innerText + ' is shown.')
	} else {
		console.log('Option [d3]' + document.getElementById('labelD' + i).innerText + ' is hidden.')
		for (j = 0; j < groupless.length; j++) {
			groupless[j].style.display = 'none';
		}
	}

	$('tr:visible').removeClass('odd').filter(':odd').addClass('odd');

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
