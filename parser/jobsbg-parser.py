import urllib3
import time
import sys
import re
from bs4 import BeautifulSoup

urllib3.disable_warnings()

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

base_string = "https://www.jobs.bg/front_job_search.php?frompage={0}&is_region=&cities%5B%5D="+str(city_data[city])+"&categories%5B%5D=15&all_type=0&all_position_level=1&all_company_type=1&keyword="
python_string = "https://www.python.org/jobs/?page={0}"

regex_results = re.compile(r'[0-9] - [0-9][0-9] от (\d+)')
python_page_regex = re.compile(r'\?page=(\d+)')
python_net_regex = re.compile(r"/jobs/\d+/")

http = urllib3.PoolManager()

with open("jobsbgparserdata", "w") as f:
	'''
		The beggining of the jobs.bg parser
	'''
	request = http.request('GET', base_string.format(0))
	soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
	for data in soup.find_all('td'):
		groups = regex_results.match(str(data.string))
		if groups:
			number_of_results = (int(groups.groups()[0]))
			break

	print("Number of results:", number_of_results)
	for x in range(0, number_of_results, 15):
		print("Query {0}-{1}".format(x, x+15))
		request = http.request('GET', base_string.format(x))
		soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
		for data in soup.find_all('a'):
			if data.get('class'):
				if data.get('class')[0] == "joblink":
					f.write("{0} | {1}\n".format(data.string, "https://www.jobs.bg/"+data.get('href')))

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
			m = python_net_regex.match(data.get('href'))
			if m:
				f.write("{0} | {1}\n".format(data.string, "https://www.python.org" + data.get('href') ) )