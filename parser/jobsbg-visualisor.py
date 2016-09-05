database_candidates = []
php_candidates = []
java_candidates = []
javascript_candidates = []
c_candidates = []
intern_candidates = []

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
	data = f.readline()

	while data:
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

		data = f.readline()

#'''
print("Database candidates: ", len(database_candidates))
for entry in database_candidates:
	print("\t",entry, end="")

print("PHP candidates: ", len(php_candidates))
for entry in php_candidates:
	print("\t",entry, end="")

print("Java candidates: ", len(java_candidates))
for entry in java_candidates:
	print("\t",entry, end="")

print("Javascript candidates: ", len(javascript_candidates))
for entry in javascript_candidates:
	print("\t",entry, end="")

print("C/C++/C# candidates: ", len(c_candidates))
for entry in c_candidates:
	print("\t",entry, end="")

print("Стажове: ", len(intern_candidates))
for entry in intern_candidates:
	print("\t",entry, end="")


#'''