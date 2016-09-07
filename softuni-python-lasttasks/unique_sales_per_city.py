city_products = {}
products = []
unique_data = {}

with open("303-sales-002.csv", "r") as f:
	data = f.readline()

	while data:
		data = data.split(",")

		if data[0] not in products:
			products.append(data[0])

		city_products.setdefault(data[2], []).append(data[0])

		data = f.readline()

for product in products:
	city = ""
	unique = 0
	for k, v in city_products.items():
		if product in v:
			city = k
			unique += 1
		if unique == 2:
			break
	if unique < 2:
		unique_data.setdefault(city, []).append(product)

for k in sorted(unique_data):
	print(k,end="")
	for product_id in sorted(unique_data[k]):
		print(",", product_id, end="")
	print("")