import urllib3
import time
import sys
import re

from html.parser import HTMLParser

urllib3.disable_warnings()

number_of_results = 0
city = 'sofia'
city_data = {
	'sofia': 1,
	'plovdiv': 2,
	'varna': 3,
	'burgas': 4,
	'blagoevgrad': 6,
	'veliko tarnovo': 7,
	'vidin': 8,
	'vraca': 9,
	'gabrovo': 10,
	'dobrich': 11,
	'kardjali': 12,
	'kjustendil': 13,
}

base_string = "https://www.jobs.bg/front_job_search.php?frompage={0}&is_region=&cities%5B%5D="+str(city_data[city])+"&categories%5B%5D=15&all_type=0&all_position_level=1&all_company_type=1&keyword="
python_string = "https://www.python.org/jobs/?page={0}"

regex_results = re.compile(r'[0-9] - [0-9][0-9] от (\d+)')
python_net_regex = re.compile(r"/jobs/\d+/")
control_regex = re.compile(r"doesnt_matter")
always_regex = re.compile(r"[\d\w\W]*")

def is_regex(regex):
	return type(control_regex) == type(regex) 


class ResultsCountGetter(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
	def handle_starttag(self, tag, attrs):
		if tag == "td":
			self.recording = 1

	def handle_endtag(self, tag):
		if tag == 'td':
			self.recording -= 1

	def handle_data(self, data):
		if self.recording:
			m = regex_results.match(data)
			if m:
				global number_of_results
				number_of_results = int(m.groups()[0])


#https://www.python.org/jobs/
class PagesGetter(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
	def handle_starttag(self, tag, attrs):
		if tag == "a" and "?page=" in attrs[0]:
			self.recording = 1
		
	def handle_endtag(self, tag):
		if tag == 'a':
			self.recording -= 1
		
	def handle_data(self, data):
		if self.recording:
			try:
				value = int(data)
				self.data.append(value)
			except Exception as e:
				pass


class PythonJobsParser(HTMLParser):
	def __init__(self, file_handler, link_appender, query_string, search_arguments, http):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
		self.link_string = ""
		self.file_handler = file_handler
		self.link_appender = link_appender
		self.query_string = query_string
		self.search_arguments = search_arguments
		self.http = http
		self.flag = 0

	def check_tag(self, tag):
		return tag in self.search_arguments

	def check_attribute(self, data, search_for):
		if is_regex(search_for):
			if search_for.search(data):
				return True
		else:
			if search_for == data:
				return True
		return False

	def handle_starttag(self, tag, attrs):
		for search_argument in self.search_arguments:
			if self.check_tag(tag):
				lists_with_requirements = self.search_arguments.get(tag)
				for i in range(len(lists_with_requirements)):
					for name, value in attrs:
						if (self.check_attribute(data = name, search_for = lists_with_requirements[i][0])
								and self.check_attribute(data = value, search_for = lists_with_requirements[i][1])):
							self.flag += 1
							if self.flag == len(lists_with_requirements):
								self.link_string = value
								self.recording = 1

	def handle_endtag(self, tag):
		for search_argument in search_arguments:
			if tag == search_argument:
				self.recording = 0
				self.flag = 0

	def handle_data(self, data):
		if self.recording:
			self.data.append(data + self.link_appender + self.link_string)

	def work(self, iteration_argument):
		request = http.request('GET', self.query_string.format(iteration_argument))
		self.feed(str(request.data, 'utf-8'))
		for line in self.data:
			self.file_handler.write("{0}\n".format(line.strip()))
		self.data = []

counter = ResultsCountGetter()

http = urllib3.PoolManager()

request = http.request('GET', base_string.format(0))
counter.feed(str(request.data, 'utf-8'))
counter.close()

print("Number of results:", number_of_results)

with open("jobsbgparserdata", "w") as f:
	search_arguments = { 'a':[["class", "joblink"], ["href", always_regex], ], }
	jobs_com_parser = PythonJobsParser(file_handler = f, search_arguments = search_arguments, http = http,
										link_appender =  " | https://www.jobs.bg/", query_string = base_string)

	for x in range(0, number_of_results, 15):
		print("Making query on result:",x,"-",x+15)
		jobs_com_parser.work(iteration_argument = x)

	f.write("SENTINEL DATA\n")
	
	page_count_getter = PagesGetter()
	search_arguments = { 'a':[["href", python_net_regex], ], }
	python_org_parser = PythonJobsParser(file_handler = f, search_arguments = search_arguments, http = http,
										link_appender =  " | https://www.python.org", query_string = python_string)
	
	request = http.request('GET', python_string.format(1))

	page_count_getter.feed(str(request.data, 'utf-8'))
	page_count_getter.close()

	pages = max(page_count_getter.data)

	for x in range(1, pages + 1):
		python_org_parser.work(iteration_argument = x)