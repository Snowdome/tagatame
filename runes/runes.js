function hide() {
	var x = document.getElementsByClassName("unreleased");
	var y = document.getElementById("hideBtn");
	if (y.innerText == "顯示未實裝刻印") {
		for(i = 0; i < x.length; i++) {
			x[i].style.display = "table-row";
		}
		y.innerHTML = "隱藏未實裝刻印";
	} else {
		for(i = 0; i < x.length; i++) {
			x[i].style.display = "none";
		}
		y.innerHTML = "顯示未實裝刻印";
	}
}