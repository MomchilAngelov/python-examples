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


class ResultsCountGetter(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
	def handle_starttag(self, tag, attrs):
		if tag == "td":
			self.recording = 1
		'''
		if tag == 'required_tag':
			for name, value in attrs:
				if name == 'somename' and value == 'somevale':
					print(name, value)
					print("Encountered the beginning of a %s tag" % tag )
					self.recording = 1 
		'''

	def handle_endtag(self, tag):
		if tag == 'td':
			self.recording -= 1
		'''
		if tag == 'required_tag':
			self.recording -=1 
			print "Encountered the end of a %s tag" % tag 
		'''
	def handle_data(self, data):
		if self.recording:
			m = regex_results.match(data)
			if m:
				global number_of_results
				number_of_results = int(m.groups()[0])


class JobsBGParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
		self.link_string = ""

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					self.link_string = value
			for name, value in attrs:
				if name == "class" and value == "joblink":
					self.recording = 1
					break
	def handle_endtag(self, tag):
		if tag == "a":
			self.recording = 0

	def handle_data(self, data):
		if self.recording:
			self.data.append(data + " | https://www.jobs.bg/" + self.link_string)


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
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0 
		self.data = []
		self.link_string = ""

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "href":
					if python_net_regex.match(value):
						self.link_string = value
						self.recording = 1


	def handle_endtag(self, tag):
		if tag == "a":
			self.recording = 0

	def handle_data(self, data):
		if self.recording:
			self.data.append(data + " | https://www.python.org/" + self.link_string)


counter = ResultsCountGetter()
parser = JobsBGParser()

http = urllib3.PoolManager()


request = http.request('GET', base_string.format(0))
counter.feed(str(request.data, 'utf-8'))
counter.close()

print("Number of results:", number_of_results)
with open("jobsbgparserdata", "w") as f:
	for x in range(0, number_of_results, 15):
		print("Making query on result:",x,"-",x+15)

		request = http.request('GET', base_string.format(x))
		parser.feed( str(request.data, 'utf-8') )

		for title in parser.data:
			f.write("{0}\n".format(title))
		parser.data = []

	f.write("SENTINEL DATA\n")
	
	page_count_getter = PagesGetter()
	python_org_parser = PythonJobsParser()
	
	request = http.request('GET', python_string.format(1))

	page_count_getter.feed(str(request.data, 'utf-8'))
	page_count_getter.close()

	pages = max(page_count_getter.data)

	for x in range(1, pages + 1):
		request = http.request('GET', python_string.format(x))
		python_org_parser.feed(str(request.data, 'utf-8'))

		for title in python_org_parser.data:
			f.write("{0}\n".format(title))
		python_org_parser.data = []