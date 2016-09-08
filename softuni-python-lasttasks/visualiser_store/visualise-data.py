import os
import sys
import pytz
import datetime
import operator

catalog = sys.argv[1]
data = sys.argv[2]

#sales data
all_sales_data = {}
#categories data
all_items_data = {}
#how much money each category got
categories_to_money = {}
cities_to_money = {}
hour_to_money = {}


all_sales_data['count'] = 0
all_sales_data['total_money'] = 0

with open(catalog) as f:
	line = f.readline()
	while line:
		line = line.split(",")

		all_items_data[line[0]] = {'gender': line[7].strip(), 'category': line[5].strip()}

		line = f.readline()

with open(data) as f:
	line = f.readline()
	while line:
		line = line.split(",")

		time = line[3]
		time = time[1:-4] + time[-3:-1]
		date = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')

		money = float(line[4].strip())

		if 'end_date' not in all_sales_data:
			all_sales_data['end_date'] = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
		else:
			if date > all_sales_data['end_date']:
				all_sales_data['end_date'] = date

		if 'begin_date' not in all_sales_data:
			all_sales_data['begin_date'] = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S%z')
		else:
			if date < all_sales_data['begin_date']:
				all_sales_data['begin_date'] = date

		all_sales_data['count'] += 1
		all_sales_data['total_money'] += money


		category = all_items_data[line[0]]['category']
		if category not in categories_to_money:
			categories_to_money[category] = money
		else:
			categories_to_money[category] += money


		city = line[2]
		if city not in cities_to_money:
			cities_to_money[city] = money
		else:
			cities_to_money[city] += money


		hour = date.replace(minute=0, second=0, microsecond=0)
		hour_to_money[hour] = hour_to_money.get(hour, 0) + money

		line = f.readline()

categories_to_money = sorted(categories_to_money.items(), key=operator.itemgetter(1))
cities_to_money = sorted(cities_to_money.items(), key=operator.itemgetter(1))
hour_to_money = sorted(hour_to_money.items(), key=operator.itemgetter(1))

print('Всички прегледани продажби:',all_sales_data['count'])
print('Обща печалба:',round(all_sales_data['total_money'], 2), '$')
print('Средна печалба:',round(all_sales_data['total_money']/all_sales_data['count'], 2), '$')
print('Дата на първата продажба', all_sales_data['begin_date'])
print('Дата на последната продажба', all_sales_data['end_date'])

best_five_by_category = reversed(categories_to_money[-5:])
best_five_by_city = reversed(cities_to_money[-5:])
best_five_by_hour = reversed(hour_to_money[-5:])

print("="*50)
print('Най-печеливши категории(5)')
for category in best_five_by_category:
	print('\t-',category[0], ":", round(float(category[1]), 2), "$")

print("="*50)
print('Най-печеливши градоре(5)')
for city in best_five_by_city:
	print('\t-',city[0], ":", round(float(city[1]), 2), "$")

print("="*50)
print('Най-печеливши часове(5)')
for hour in best_five_by_hour:
	print('\t-',hour[0], ":", round(float(hour[1]), 2), "$")