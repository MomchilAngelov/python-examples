import operator
import sys

all_data = {}
try:
	liters = float(input("Литри: "))
except:
	print("Invalid input")

with open(input("Данни: "), "r") as f:
	for line in f:
		if line == "\n":
			continue

		data = line.split(" ")[1].split(",")
		name = data[0]
		r = float(data[1]) / 10
		h = float(data[2]) / 10
		area = r*r * 3.14 * h
		all_data[name] = area

tuples = sorted(all_data.items(), key=operator.itemgetter(1))

for pair in tuples:
	if pair[1] > liters:
		print("Бидонче:",pair[0])
		sys.exit()
print("NO SUITABLE CONTAINER")
