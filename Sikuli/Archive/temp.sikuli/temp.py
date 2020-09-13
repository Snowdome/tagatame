list = ("Nothing selected","Google","Microsoft","Apple")

choice = select("Which company would you like to work for?", options = list)

if choice == list[0]:

    popup("You selected none of the companies")

    exit(1)