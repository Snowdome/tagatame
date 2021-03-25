autoRepeat = "autoRepeat.png"
arComplete = "arComplete.png"
if exists(autoRepeat):
	if Region(find(autoRepeat).x, find(autoRepeat).y - 65, find(autoRepeat).w, find(autoRepeat).h + 65).exists(arComplete):
		print("complete")
	else:
		print("incomeplete")
else:
	print("not exist")