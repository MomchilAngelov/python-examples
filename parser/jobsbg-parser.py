import urllib3
import time
import sys
import re
from bs4 import BeautifulSoup
import threading

urllib3.disable_warnings()

threadLock = threading.Lock()

n_threads = 3
threads = []

class NetworkParser(threading.Thread):
	def __init__(self, http, url, start_value, end_value, file_handler):
		threading.Thread.__init__(self)
		self.http = http
		self.url = url
		self.start_value = start_value
		self.end_value = end_value
		self.file_handler = file_handler
		self.parsed_data = []

	def run(self):
		for x in range(self.start_value, self.end_value, 15):
			print("Making a query in the range: {0} - {1}".format(x, x + 15))
			request = http.request('GET', self.url.format(x))
			soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
			for data in soup.find_all('a'):
				if data.get('class'):
					if data.get('class')[0] == "joblink":
						temp_list = [data.string, data.get('href')]
						self.parsed_data.append(temp_list)
			threadLock.acquire()
			for my_list in self.parsed_data:
				f.write("{0} | {1}\n".format(my_list[0], "https://www.jobs.bg/" + my_list[1]))	
			threadLock.release()
			self.parsed_data = []

number_of_results = 0
max_page = []
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

jobs_bg_string = "https://www.jobs.bg/front_job_search.php?frompage={0}&is_region=&cities%5B%5D="\
					+ str(city_data[city]) + \
					"&categories%5B%5D=15&all_type=0&all_position_level=1&all_company_type=1&keyword="
python_string = "https://www.python.org/jobs/?page={0}"

jobs_bg_regex_results = re.compile(r'[0-9] - [0-9][0-9] от (\d+)')
python_page_regex = re.compile(r'\?page=(\d+)')
python_jobs_getter_regex = re.compile(r"/jobs/\d+/")


''' Start of "main" '''
http = urllib3.PoolManager()

with open("jobsbgparserdata", "w") as f:
	'''
		The beggining of the jobs.bg parser
	'''
	request = http.request('GET', jobs_bg_string.format(0))
	soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
	for data in soup.find_all('td'):
		groups = jobs_bg_regex_results.match(str(data.string))
		if groups: 
			number_of_results = (int(groups.groups()[0]))
			break

	for k in range(n_threads):
		thread = NetworkParser(http = http, url = jobs_bg_string, 
								start_value = (0+k) * int(number_of_results/n_threads),
								  end_value = (1+k) * int(number_of_results/n_threads),
								  file_handler = f)
		threads.append(thread)

	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()

	f.write("SENTINEL DATA\n")
	'''
		The beggining of the python.org parser
	'''
	request = http.request('GET', python_string.format(1))
	soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
	for link_href in soup.find_all('a'):
		data = link_href.get('href')
		if '?page=' in data:
			m = python_page_regex.match(data)
			max_page.append(int(m.groups()[0]))

	max_page = max(max_page)
	for x in range(1, max_page+1):
		print("Page {0}".format(x))
		request = http.request('GET', python_string.format(x))
		soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
		for data in soup.find_all('a'):
			href = data.get('href')
			m = python_jobs_getter_regex.match(href)
			if m:
				full_href = "https://www.python.org" + href
				f.write("{0} | {1}\n".format(data.string, full_href))