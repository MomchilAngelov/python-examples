import collections

date_to_cities = {}
cities = []
missing_data = {}

with open("city-data.csv", "r") as f:
	for line in f:
		data = line.split(",")

		date_to_cities.setdefault(data[0], []).append(data[1])

for k, v in date_to_cities.items():
	for city in v:
		if city not in cities:
			cities.append(city)

for k, v in date_to_cities.items():
	for city in cities:
		if city not in v:
			missing_data.setdefault(k, []).append(city)

if missing_data:
	for k in sorted(missing_data):
		print(k, end="")
		for city in sorted(missing_data[k]):
			print(",",city, end="")
		print("")
else:
	print("ALL DATA AVAILABLE")