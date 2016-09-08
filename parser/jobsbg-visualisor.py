database_candidates = ['Database candidates']
php_candidates = ['PHP candidates']
java_candidates = ['JAVA candidates']
javascript_candidates = ['JavaScript candidates']
c_candidates = ['C/C++/C# candidates']
python_candidates = ['Python candidates']
intern_candidates = ['Intern candidates']

all_candidates = [database_candidates, php_candidates, javascript_candidates, 
					java_candidates, c_candidates, python_candidates, intern_candidates]

def database_candidate(string):
	if "MySQL" in string:
		return 1
	if "Database" in string:
		return 1
	if "Data" in string:
		return 1
	return 0

def php_candidate(string):
	if "php" in string:
		return 1
	if "PHP" in string:
		return 1
	return 0

def java_candidate(string):
	if "Java " in string:
		return 1
	if "java " in string:
		return 1
	if "JAVA " in string:
		return 1
	return 0

def c_candidate(string):
	if "C/C++/C#" in string:
		return 1
	if "C/C++" in string:
		return 1
	if "C " in string:
		return 1
	if "C++ " in string:
		return 1
	if "C# " in string:
		return 1
	if "objective C" in string:
		return 1
	if "objective-C" in string:
		return 1
	return 0


def javascript_candidate(string):
	if "Javascript" in string:
		return 1
	if "JavaScript" in string:
		return 1
	if "javascript" in string:
		return 1
	if "JAVASCRIPT" in string:
		return 1
	if "ECMASCRIPT" in string:
		return 1
	if "ACTIONSCRIPT" in string:
		return 1
	if "COFFEESCRIPT" in string:
		return 1
	return 0

def python_candidate(string):
	if "Python" in string:
		return 1
	if "python" in string:
		return 1
	if "Django" in string:
		return 1
	if "Python/Django" in string:
		return 1
	if "django" in string:
		return 1
	return 0

def intern_candidate(string):
	if "Стажант" in string:
		return 1
	if "Стаж" in string:
		return 1
	if "стажант" in string:
		return 1
	if "стаж" in string:
		return 1
	if "Intern" in string:
		return 1
	if "intern" in string:
		return 1
	if "INTERN" in string:
		return 1
	return 0


with open("jobsbgparserdata", "r") as f:
	for data in f:
		if database_candidate(data):
			database_candidates.append(data)

		if php_candidate(data):
			php_candidates.append(data)

		if java_candidate(data):
			java_candidates.append(data)

		if javascript_candidate(data):
			javascript_candidates.append(data)

		if c_candidate(data):
			c_candidates.append(data)

		if intern_candidate(data):
			intern_candidates.append(data)

		if python_candidate(data):
			python_candidates.append(data)

with open("visualised_results.html", "w") as f:
	f.write("<html>")
	f.write("<head>")
	f.write("<title>")
	f.write("Визуализирани данни!")
	f.write("</title>")
	f.write("<style>")
	f.write("table, th, td {border: 1px solid black}")
	f.write("</style>")
	f.write("<meta charset='UTF-8'>")
	f.write("</head>")
	f.write("<body>")
	for candidates in all_candidates:

		f.write("<h1>")
		f.write(candidates.pop(0))
		f.write("</h1>")

		f.write("<table>")

		f.write("<tr>")
		f.write("<th>")
		f.write("Титла")
		f.write("</th>")
		f.write("<th>")
		f.write("Линк към работата")	
		f.write("</th>")
		f.write("</tr>")

		for entry in candidates:
			entry = entry.split("|")

			f.write("<tr>")

			
			f.write("<td>")
			f.write(entry[0])
			f.write("</td>")
			
			f.write("<td>")
			f.write("<a href='{0}' target='blank'>".format(entry[1]))
			f.write("Линк")
			f.write("</a>")
			f.write("</td>")


			f.write("</tr>")

		f.write("</table>")
	f.write("</body>")
	f.write("</html>")


'''
print("Database candidates: ", len(database_candidates))
for entry in database_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("PHP candidates: ", len(php_candidates))
for entry in php_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("Java candidates: ", len(java_candidates))
for entry in java_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("Javascript candidates: ", len(javascript_candidates))
for entry in javascript_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("C/C++/C# candidates: ", len(c_candidates))
for entry in c_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("Python candidates: ", len(python_candidates))
for entry in python_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")

print("Стажове: ", len(intern_candidates))
for entry in intern_candidates:
	entry = entry.split("|")
	size_of_string = len(entry[0])
	maximum_size = 100
	number_of_spaces = maximum_size - size_of_string
	print("\t",entry[0]," "*number_of_spaces, entry[1].strip() , end="\n")
'''