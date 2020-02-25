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
