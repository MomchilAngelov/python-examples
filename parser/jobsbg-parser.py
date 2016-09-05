import urllib3
import time
import sys
import re

from html.parser import HTMLParser

begin = int(time.time())
number_of_results = 0
base_string = "https://www.jobs.bg/front_job_search.php?frompage={0}&zone_id=9&is_region=0&all_cities=0&categories%5B0%5D=15&all_position_level=1&all_company_type=1&keyword=&last=0#paging"
regex_results = re.compile(r'[0-9] - [0-9][0-9] от (\d+)')


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

	def handle_starttag(self, tag, attrs):
		if tag == "a":
			for name, value in attrs:
				if name == "class" and value == "joblink":
					self.recording = 1
					break
	def handle_endtag(self, tag):
		if tag == "a":
			self.recording = 0

	def handle_data(self, data):
		if self.recording:
			self.data.append(data)


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