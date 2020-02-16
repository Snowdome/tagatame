function hide() {
  var x = document.getElementById("patchNote");
  var y = document.getElementById("hideBtn").innerHTML;
  if (x.style.display === "none") {
    x.style.display = "block";
	document.getElementById("hideBtn").innerHTML = "Hide";
  } else {
    x.style.display = "none";
	document.getElementById("hideBtn").innerHTML = "Show";
  }
}

function score() {
	var b1, b2, b0, s1, s2, s3, s4, s5, s6, s7, s0, e01, e02, e03, e04, e05, e06, e07, e08, e09, e10, e11, e12, e13, e14, e15, pm, sin, ex;
	b1 = 0; b2 = 0;	b0 = 0;
	s1 = 0; s2 = 0; s3 = 0; s4 = 0; s5 = 0; s6 = 0; s7 = 0; s0 = 0;
	e01 = 0; e02 = 0; e03 = 0; e04 = 0; e05 = 0; e06 = 0; e07 = 0; e08 = 0; e09 = 0; e10 = 0; e11 = 0; e12 = 0; e13 = 0; e14 = 0; e15 = 0;
	pm = 0; sin = 0; ex = 0;
	pm = document.querySelector('input[name = "pm"]:checked').value;
	sin = document.querySelector('input[name = "sin"]:checked').value;
	
	if (pm == "phy") {
		b1 = 1;
	}	else if (pm == "mag") {
		b2 = 1;
	}	else	{
		b0 = 1;
	}
	
	if (sin == "envy")	{
		s1 = 1;
	}	else if (sin == "sloth") {
		s2 = 1;
	}	else if (sin == "lust") {
		s3 = 1;
	}	else if (sin == "gluttony") {
		s4 = 1;
	}	else if (sin == "wrath") {
		s5 = 1;
	}	else if (sin == "greed") {
		s6 = 1;
	}	else if (sin == "pride") {
		s7 = 1;
	}	else if (sin == "any") {
		s0 = 1;
	}
	var e01 = document.querySelector("#ex01").checked;
	var e02 = document.querySelector("#ex02").checked;
	var e03 = document.querySelector("#ex03").checked;
	var e04 = document.querySelector("#ex04").checked;
	var e05 = document.querySelector("#ex05").checked;
	var e06 = document.querySelector("#ex06").checked;
	var e07 = document.querySelector("#ex07").checked;
	var e08 = document.querySelector("#ex08").checked;
	var e09 = document.querySelector("#ex09").checked;
	var e10 = document.querySelector("#ex10").checked;
	var e11 = document.querySelector("#ex11").checked;
	var e12 = document.querySelector("#ex12").checked;
	var e13 = document.querySelector("#ex13").checked;
	var e14 = document.querySelector("#ex14").checked;
	var e15 = document.querySelector("#ex15").checked;
	
	document.getElementById('m001').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m002').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m003').innerHTML = (b1*0+b2*0+b0*0) + (s1*15+s2*0+s3*0+s4*0+s5*15+s6*0+s7*0+s0*15) + (e01*30+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m004').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m005').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m006').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m007').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m008').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m009').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m010').innerHTML = (b1*30+b2*0+b0*30) + (s1*30+s2*0+s3*0+s4*30+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*30+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m011').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*10+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m012').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*30+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m013').innerHTML = (b1*50+b2*0+b0*50) + (s1*0+s2*0+s3*0+s4*30+s5*30+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m014').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*60+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m015').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*40+s4*20+s5*0+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*20+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m016').innerHTML = (b1*15+b2*15+b0*15) + (s1*30+s2*0+s3*30+s4*0+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m017').innerHTML = (b1*0+b2*20+b0*20) + (s1*0+s2*0+s3*20+s4*20+s5*20+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*20+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m018').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*10+s5*0+s6*0+s7*20+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m019').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*0+s4*30+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m020').innerHTML = (b1*50+b2*0+b0*50) + (s1*20+s2*0+s3*0+s4*20+s5*20+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m021').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*20+s5*0+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*20+e13*0+e14*0+e15*0);
	document.getElementById('m022').innerHTML = (b1*0+b2*40+b0*40) + (s1*20+s2*0+s3*20+s4*20+s5*0+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m023').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m024').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m025').innerHTML = (b1*20+b2*0+b0*20) + (s1*20+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m026').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m027').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m028').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m029').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*60+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*30+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m030').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*40+s6*20+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m031').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m032').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m033').innerHTML = (b1*0+b2*0+b0*0) + (s1*20+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m034').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m035').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m036').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m037').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m038').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*20+s5*40+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*20+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m039').innerHTML = (b1*30+b2*0+b0*30) + (s1*10+s2*0+s3*10+s4*0+s5*10+s6*0+s7*0+s0*10) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m040').innerHTML = (b1*20+b2*0+b0*20) + (s1*30+s2*0+s3*0+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*0+e02*20+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m041').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m042').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m043').innerHTML = (b1*20+b2*0+b0*20) + (s1*30+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m044').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m045').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m046').innerHTML = (b1*15+b2*0+b0*15) + (s1*20+s2*0+s3*0+s4*0+s5*20+s6*20+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m047').innerHTML = (b1*15+b2*0+b0*15) + (s1*20+s2*0+s3*0+s4*0+s5*40+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m048').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m049').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m050').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m051').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*40+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m052').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m053').innerHTML = (b1*30+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*60+s6*0+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m054').innerHTML = (b1*30+b2*20+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*30+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m055').innerHTML = (b1*30+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*60+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m056').innerHTML = (b1*50+b2*0+b0*50) + (s1*30+s2*0+s3*0+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m057').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m058').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m059').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m060').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m061').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m062').innerHTML = (b1*30+b2*30+b0*30) + (s1*30+s2*30+s3*0+s4*0+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*30+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m063').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m064').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m065').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m066').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m067').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m068').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m069').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m070').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m071').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*30+s3*0+s4*0+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m072').innerHTML = (b1*40+b2*0+b0*40) + (s1*0+s2*40+s3*0+s4*0+s5*0+s6*20+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*30+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m073').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m074').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*0+s7*30+s0*30) + (e01*0+e02*0+e03*20+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m075').innerHTML = (b1*50+b2*0+b0*50) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*20+s7*40+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m076').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*0+s7*30+s0*30) + (e01*0+e02*0+e03*20+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m077').innerHTML = (b1*0+b2*20+b0*20) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*20+s7*40+s0*40) + (e01*30+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m078').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*20+s7*40+s0*40) + (e01*40+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*20+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m079').innerHTML = (b1*0+b2*30+b0*30) + (s1*0+s2*0+s3*20+s4*0+s5*0+s6*0+s7*40+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*20+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m080').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*20+s5*0+s6*0+s7*40+s0*40) + (e01*0+e02*0+e03*20+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m081').innerHTML = (b1*30+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*60+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m082').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*60+s0*60) + (e01*0+e02*0+e03*0+e04*40+e05*40+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*10+e13*0+e14*0+e15*0);
	document.getElementById('m083').innerHTML = (b1*0+b2*50+b0*50) + (s1*20+s2*0+s3*0+s4*0+s5*0+s6*0+s7*40+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m084').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*0+s4*0+s5*30+s6*0+s7*30+s0*30) + (e01*20+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m085').innerHTML = (b1*0+b2*40+b0*40) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*20+s7*40+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m086').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*20+s4*0+s5*20+s6*0+s7*20+s0*20) + (e01*40+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m087').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m088').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m089').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m090').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m091').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m092').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m093').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m094').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m095').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m096').innerHTML = (b1*0+b2*30+b0*30) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m097').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m098').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m099').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m100').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m101').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m102').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m103').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m104').innerHTML = (b1*30+b2*0+b0*30) + (s1*20+s2*0+s3*20+s4*0+s5*0+s6*20+s7*0+s0*20) + (e01*40+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m105').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*10+s4*0+s5*20+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m106').innerHTML = (b1*30+b2*30+b0*30) + (s1*0+s2*0+s3*60+s4*0+s5*0+s6*0+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*40+e15*0);
	document.getElementById('m107').innerHTML = (b1*40+b2*0+b0*40) + (s1*0+s2*0+s3*0+s4*0+s5*60+s6*0+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*40+e15*0);
	document.getElementById('m108').innerHTML = (b1*40+b2*0+b0*40) + (s1*0+s2*0+s3*20+s4*0+s5*0+s6*0+s7*40+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m109').innerHTML = (b1*50+b2*0+b0*50) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*40+s7*20+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*20+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m110').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m111').innerHTML = (b1*20+b2*20+b0*20) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*60+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m112').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m113').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m114').innerHTML = (b1*20+b2*0+b0*20) + (s1*20+s2*20+s3*0+s4*0+s5*0+s6*20+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*50+e14*0+e15*0);
	document.getElementById('m115').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*10+s6*0+s7*20+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m116').innerHTML = (b1*60+b2*0+b0*60) + (s1*30+s2*0+s3*0+s4*0+s5*0+s6*30+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m117').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m118').innerHTML = (b1*50+b2*0+b0*50) + (s1*0+s2*0+s3*0+s4*20+s5*30+s6*0+s7*10+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*30+e14*0+e15*0);
	document.getElementById('m119').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*60+s0*60) + (e01*0+e02*0+e03*0+e04*40+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m120').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m121').innerHTML = (b1*40+b2*0+b0*40) + (s1*0+s2*0+s3*30+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*20+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m122').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m123').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*60+s3*0+s4*0+s5*0+s6*0+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*20+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m124').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m125').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m126').innerHTML = (b1*0+b2*30+b0*30) + (s1*20+s2*0+s3*0+s4*0+s5*40+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*20+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m127').innerHTML = (b1*0+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*40+s5*20+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*30+e06*0+e07*0+e08*0+e09*0+e10*0+e11*20+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m128').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m129').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*30+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m130').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m131').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m132').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m133').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m134').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m135').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m136').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m137').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m138').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m139').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m140').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m141').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m142').innerHTML = (b1*0+b2*40+b0*40) + (s1*0+s2*30+s3*0+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*10+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m143').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m144').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m145').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m146').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m147').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m148').innerHTML = (b1*20+b2*20+b0*20) + (s1*30+s2*0+s3*0+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m149').innerHTML = (b1*30+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*30+s5*0+s6*0+s7*30+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*40);
	document.getElementById('m150').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*0+s4*40+s5*20+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m151').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*20+s3*0+s4*0+s5*40+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m152').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m153').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m154').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*40+s4*0+s5*0+s6*0+s7*20+s0*40) + (e01*20+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m155').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m156').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m157').innerHTML = (b1*0+b2*0+b0*0) + (s1*20+s2*0+s3*0+s4*0+s5*20+s6*20+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m158').innerHTML = (b1*40+b2*0+b0*40) + (s1*0+s2*0+s3*20+s4*20+s5*20+s6*0+s7*0+s0*20) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m159').innerHTML = (b1*20+b2*20+b0*20) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*60+s7*0+s0*60) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m160').innerHTML = (b1*0+b2*40+b0*40) + (s1*0+s2*0+s3*30+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*30+e05*30+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m161').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*60+s7*0+s0*60) + (e01*40+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m162').innerHTML = (b1*20+b2*0+b0*20) + (s1*30+s2*0+s3*0+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*30+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*10+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m163').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*30+s7*0+s0*30) + (e01*30+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m164').innerHTML = (b1*30+b2*0+b0*30) + (s1*10+s2*10+s3*0+s4*0+s5*0+s6*10+s7*0+s0*10) + (e01*20+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m165').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m166').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m167').innerHTML = (b1*0+b2*30+b0*30) + (s1*0+s2*0+s3*0+s4*20+s5*0+s6*40+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m168').innerHTML = (b1*30+b2*0+b0*30) + (s1*0+s2*0+s3*0+s4*30+s5*0+s6*30+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*20+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m169').innerHTML = (b1*30+b2*0+b0*30) + (s1*30+s2*0+s3*0+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*30+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m170').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m171').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m172').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m173').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m174').innerHTML = (b1*60+b2*0+b0*60) + (s1*0+s2*0+s3*0+s4*0+s5*20+s6*40+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m175').innerHTML = (b1*0+b2*0+b0*0) + (s1*15+s2*0+s3*0+s4*0+s5*15+s6*0+s7*0+s0*15) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m176').innerHTML = (b1*20+b2*0+b0*20) + (s1*0+s2*0+s3*0+s4*40+s5*20+s6*0+s7*0+s0*40) + (e01*0+e02*20+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m177').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m178').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m179').innerHTML = (b1*0+b2*30+b0*30) + (s1*30+s2*0+s3*0+s4*0+s5*30+s6*0+s7*0+s0*30) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m180').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m181').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m182').innerHTML = (b1*0+b2*0+b0*0) + (s1*0+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*0) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m183').innerHTML = (b1*15+b2*0+b0*15) + (s1*40+s2*0+s3*0+s4*0+s5*0+s6*20+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m184').innerHTML = (b1*30+b2*0+b0*30) + (s1*20+s2*0+s3*0+s4*0+s5*40+s6*0+s7*0+s0*40) + (e01*0+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*10+e12*0+e13*0+e14*0+e15*0);
	document.getElementById('m185').innerHTML = (b1*20+b2*0+b0*20) + (s1*60+s2*0+s3*0+s4*0+s5*0+s6*0+s7*0+s0*60) + (e01*20+e02*0+e03*0+e04*0+e05*0+e06*0+e07*0+e08*0+e09*0+e10*0+e11*0+e12*0+e13*0+e14*0+e15*0);
}

function sortTableByString(n) {
	var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
	table = document.getElementById("mementos");
	switching = true;
	//Set the sorting direction to descending:
	dir = "desc"; 
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
			x = rows[i].getElementsByTagName("TD")[n];
			y = rows[i + 1].getElementsByTagName("TD")[n];
			/*check if the two rows should switch place, based on the direction, asc or desc:*/
			if (dir == "asc") {
				if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
					//if so, mark as a switch and break the loop:
					shouldSwitch= true;
					break;
				}
			} else if (dir == "desc") {
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
			switchcount ++;			
		} else {
			/*If no switching has been done AND the direction is "desc", set the direction to "asc" and run the while loop again.*/
			if (switchcount == 0 && dir == "desc") {
				dir = "asc";
				switching = true;
			}
		}
	}
}

function sortTableByNumber(n) {
	var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
	table = document.getElementById("mementos");
	switching = true;
	//Set the sorting direction to descending:
	dir = "desc"; 
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
			x = rows[i].getElementsByTagName("TD")[n];
			y = rows[i + 1].getElementsByTagName("TD")[n];
			/*check if the two rows should switch place, based on the direction, asc or desc:*/
			if (dir == "asc") {
				if (Number(x.innerHTML) > Number(y.innerHTML)) {
					//if so, mark as a switch and break the loop:
					shouldSwitch= true;
					break;
				}
			} else if (dir == "desc") {
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
			switchcount ++;			
		} else {
			/*If no switching has been done AND the direction is "desc", set the direction to "asc" and run the while loop again.*/
			if (switchcount == 0 && dir == "desc") {
				dir = "asc";
				switching = true;
			}
		}
	}
}