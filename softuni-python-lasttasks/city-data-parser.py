import collections

date_to_cities = {}
cities = []
missing_data = {}

with open("city-data.csv", "r") as f:
	data = f.readline()

	while data:
		data = data.split(",")
		if data[0] in date_to_cities:
			date_to_cities[data[0]].append(data[1])
		else:
			date_to_cities[data[0]] = [data[1]]
		data = f.readline()

for k, v in date_to_cities.items():
	for city in v:
		if city not in cities:
			cities.append(city)

for k, v in date_to_cities.items():
	for city in cities:
		if city not in v:
			if k not in missing_data:
				missing_data[k] = [city]
			else:
				missing_data[k].append(city)

if missing_data:
	for k in sorted(missing_data):
		print(k, end="")
		for city in sorted(missing_data[k]):
			print(",",city, end="")
		print("")
else:
	print("ALL DATA AVAILABLE")