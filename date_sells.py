import datetime

data = {}

with open("sales.csv") as f:
	line = f.readline()
	while line:
		entry = line.split(",")
		time = datetime.datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S')
		hour = int(time.hour)
		#change to time.day to get the most profitable date
		money = int(round(float(entry[1].strip())))
		if hour in data:
			data[hour] += money
		else:
			data[hour] = money
		line = f.readline()

profit = 0
hour = 0
for k, v in data.items():
	if v > profit:
		profit = v
		hour = k

print("Most profitable hour is ", hour, " with a profit of ", profit)