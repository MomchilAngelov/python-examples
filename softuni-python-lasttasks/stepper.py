import sys

x = 0
y = 0

with open(sys.argv[1], "r") as f:
	for line in f:
		if line == "\n":
			continue

		data = line.split(" ")
		if data[0] == "up":
			y += float(data[1])
		if data[0] == "down":
			y -= float(data[1])

		if data[0] == "left":
			x -= float(data[1])
		if data[0] == "right":
			x += float(data[1])
	
	print("x: ",round(x, 3),"\ny:", round(y, 3))
