import sys

x = 0
y = 0

with open(sys.argv[1], "r") as f:
	data = f.readline()

	while data:
		if data == "\n":
			data = f.readline()
			continue

		data = data.split(" ")
		if data[0] == "up":
			y += float(data[1])
		if data[0] == "down":
			y -= float(data[1])

		if data[0] == "left":
			x -= float(data[1])
		if data[0] == "right":
			x += float(data[1])
		data = f.readline()
	
	print("x: ",round(x, 3),"\ny:", round(y, 3))
