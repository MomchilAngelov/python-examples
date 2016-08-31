data = {}
with open('catalog_full.csv', 'r') as f:
	line = f.readline()
	while line:
		items = line.split(",")
		gender = items[5]
		money = float(items[6][0:-1])
		gender_data = data.get(gender)
		if gender_data is None:
			small_data = [money, 1]
			data[gender] = small_data
		else:
			small_data = [data[gender][0]+money, data[gender][1]+1]
			data[gender] = [data[gender][0]+money, data[gender][1]+1]
		
		line = f.readline()

for k in data:
	total = data[k][0]
	number = data[k][1]
	del data[k][1]
	average = total/number
	data[k][0] = average

for k, v in data.items():
	print("Средната печалба на категория за пола ",k," е ", round(v[0], 2))
