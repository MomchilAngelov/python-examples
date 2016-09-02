import os
import sys
import re

#python3 python_find.py ../ \\w\\.py

def fits_criteria(found_file, look_for_file):
	if re.search(look_for_file, found_file) is None:
		return False
	else :
		return True

error_check = len(sys.argv)
print(error_check)

if not error_check == 3:
	print("Invalid input: python_find.py <search_dir> <search_file>")
	sys.exit()

directory = sys.argv[1]
searched_file = re.compile(sys.argv[2])
results = []
dir_count = 1

for dirpath, dirnames, filenames in os.walk(directory):
	print("Директория {}".format(dir_count))
	for file in filenames:
		if fits_criteria(file, searched_file):
			results.append(os.path.abspath(os.path.join(dirpath, file)))
	dir_count += 1
for file in results:
	print(file)