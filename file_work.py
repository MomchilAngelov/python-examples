i = 0

with open('./downloader_data/places', 'r', encoding = 'utf-8') as file:
	for line in file:
		if "official-portal.com" not in line:
			print(line, end="")
			i += 1
print("Number of links: " + str(i))