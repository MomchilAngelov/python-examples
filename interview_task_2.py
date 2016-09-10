import collections
import sys

#user defined data
max_representation = 20

biggest_number = 0
value_per_ds = 0
input_data = input("Please enter some text: ")

print("\nMost common letters: \n")

data = collections.defaultdict(int)
for letter in input_data.upper():
	data[letter] += 1

biggest_number = data[max(data, key=data.get)]
value_per_ds = max_representation/biggest_number

for idx, k in enumerate(sorted(data, key=data.get, reverse=True)):
	if idx == 20:
		break
	print( "{0}: {1} {2}".format(k, data[k],
								 "#"*int( (data[k] * value_per_ds) )))
else:
	print("That was all the data")
	sys.exit()
print("There was more data, but only 20 made it to the top!")
