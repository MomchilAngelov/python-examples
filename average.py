inputs = 0
l = []

while True:
	try:
		val = input("Mоля въведете цена: ")
		if val == "stop":
			break
		val = int(val)
		l.append(val)
		inputs += 1
	except Exception as e:
		print("Моля въведете реално число!")

if inputs < 4:
	print("Твърде малко данни!")

l.remove(max(l))
l.remove(min(l))
all_val = 0
for val in l:
	all_val+= val
print("Средна цена {0}".format(all_val/(inputs-2)))