from time import gmtime, strftime

database_candidates = ['Database candidates']
php_candidates = ['PHP candidates']
java_candidates = ['JAVA candidates']
javascript_candidates = ['JavaScript candidates']
c_candidates = ['C/C++/C# candidates']
python_candidates = ['Python candidates']
intern_candidates = ['Intern candidates']
frontend_candidates = ['Front-End candidates']

python_org_candidates = ['Python.org candidates']

all_candidates = [database_candidates, php_candidates, javascript_candidates, 
					java_candidates, c_candidates, python_candidates, intern_candidates, 
						frontend_candidates,python_org_candidates, ]
all_candidates_names = ['database_candidate', 'php_candidate', 'javascript_candidate', 
						'java_candidate', 'c_candidate', 'python_candidate', 'intern_candidate', 
							'frontend_candidate',]
def frontend_candidate(string):
	if "FrontEnd" in string.upper():
		return 1
	if "Front-End" in string.upper():
		return 1
	if "Front End" in string.upper():
		return 1
	return 0


def database_candidate(string):
	if "SQL" in string.upper():
		return 1
	if "MYSQL" in string.upper():
		return 1
	if "DATA" in string.upper():
		return 1
	if "POSTGRE" in string.upper():
		return 1
	return 0

def php_candidate(string):
	if "PHP" in string.upper():
		return 1
	return 0

def java_candidate(string):
	if "JAVA " in string.upper():
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
	if "JAVASCRIPT" in string.upper():
		return 1
	if "ECMASCRIPT" in string.upper():
		return 1
	if "ACTIONSCRIPT" in string.upper():
		return 1
	if "COFFEESCRIPT" in string.upper():
		return 1
	return 0

def python_candidate(string):
	if "PYTHON" in string.upper():
		return 1
	if "DJANGO" in string.upper():
		return 1
	if "TORNADO" in string.upper():
		return 1
	return 0

def intern_candidate(string):
	if "СТАЖ" in string.upper():
		return 1
	if "INTERN" in string.upper():
		return 1
	return 0


with open("jobsbgparserdata", "r") as f:
	flag_for_not_jobs_bg = 0
	for data in f:
		data = data.strip()
		if data == "SENTINEL DATA":
			flag_for_not_jobs_bg = 1
			continue
		if flag_for_not_jobs_bg:
			python_org_candidates.append(data)
		else:
			for name in all_candidates_names:
				if eval(name+"(data)"):
					eval(name+"s.append(data)")

with open("reports/{0}visualised_results.html".format(strftime("%Y-%m-%d %H:%M:%S", gmtime())), "w") as f:
	f.write("<html>")
	f.write("<head>")
	f.write("<title>")
	f.write("Визуализирани данни!")
	f.write("</title>")
	f.write("<style>")
	f.write("table, th, td {border: 1px solid black}\na:visited {color: red}\nbody table {font-size: 20px;}\n")
	f.write("table tr:nth-child(2n+3) {background-color: #D6D6D8}")
	f.write("</style>")
	f.write("<meta charset='UTF-8'>")
	f.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.0/jquery.min.js'></script>")
	f.write("<script>$(document).ready(function(){$('h1').click(function(){$(this).next().toggle()})})</script>")
	f.write("</head>")
	f.write("<body>")
	for candidates in all_candidates:

		f.write("<h1>")
		f.write(candidates.pop(0) + " - брой обяви: " + str(len(candidates)))
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
			f.write("<a href='{0}' target='_blank'>".format(entry[1]))
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
'''
json_data = {}
for candidate in all_candidates:
	candidate_entry = candidate.pop(0)
	json_data[candidate_entry] = []
	for entry in candidate:
		try:
			data = entry.split("|")
			entry_data_json = {'url': data[1].strip(), 'title': data[0].strip()}
			json_data[candidate_entry].append(entry_data_json)
		except Exception as e:
			print(e)
print("\"",json_data,"\"", end="")
'''