import math
count = 0
data = []
while True:
    try:
        val = float(input("Вход:"))
    except: 
        print("Невалиден Вход")
    data.append(val)
    if count == 3:
        break
    count += 1

area_paper = data[0] - data[0] * 0.098
area_box = data[1] * data[2] * 2 + data[2] * data[3] * 2 + data[1] * data[3] * 2

list_count = math.ceil(area_box/area_paper)
print(list_count)