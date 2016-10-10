'''
	Parser and writer to a file
'''
# With beatifull soup - 9 minutes ~beatifull soup is faster then the library its build upon - nice :Д
# 

import re
import threading
import urllib3
from bs4 import BeautifulSoup

class NetworkParser(threading.Thread):
    '''
        NetworkParser!
    '''
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
            request = self.http.request('GET', self.url.format(x))
            self.soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
            for data in self.soup.find_all('a'):
                if data.get('class'):
                    if data.get('class')[0] == "joblink":
                        temp_list = [data.string, data.get('href')]
                        self.parsed_data.append(temp_list)

            THREAD_LOCK.acquire()

            for my_list in self.parsed_data:
                f.write("{0} | {1}\n".format(my_list[0], "https://www.jobs.bg/" + my_list[1]))
            THREAD_LOCK.release()
            
            self.parsed_data = []

if __name__ == '__main__':

    urllib3.disable_warnings()

    THREAD_LOCK = threading.Lock()

    NUMBER_OF_THREADS = 4
    THREADS = []


    NUMBER_OF_RESULTS = 0
    MAX_PAGE = []
    CITY = 'sofia'
    CITY_DATA = {
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

    JOBS_BG_STRING = "https://www.jobs.bg/front_job_search.php?frompage={0}&is_region=&cities"\
    					+"%5B%5D=" + str(CITY_DATA[CITY]) + \
                        "&categories%5B%5D=15&all_type=0&all_position_level=1&all_company_type=1"+\
                        "&keyword="

    PYTHON_STRING = "https://www.python.org/jobs/?page={0}"
    '''
    JOBS_BG_STRING = "https://www.jobs.bg/front_job_search.php?frompage={0}&is_region=&all_cities"\
    +"=0&all_categories=0&all_type=0&all_position_level=1&all_company_type=1&keyword="
    '''

    JOBS_BG_REGEX_RESULT = re.compile(r'[0-9] - [0-9][0-9] от (\d+)')
    PYTHON_PAGE_REGEX = re.compile(r'\?page=(\d+)')
    JOBS_BG_REGEX = re.compile(r"/jobs/\d+/")

    HTTP = urllib3.PoolManager()

    with open("jobsbgparserdata", "w") as f:
        request = HTTP.request('GET', JOBS_BG_STRING.format(0))
        soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
        for data in soup.find_all('td'):
            groups = JOBS_BG_REGEX_RESULT.match(str(data.string))
            if groups:
                NUMBER_OF_RESULTS = (int(groups.groups()[0]))
                break
        for k in range(NUMBER_OF_THREADS):
            thread = NetworkParser(http=HTTP, url=JOBS_BG_STRING,
                                   start_value=(0+k) * int(NUMBER_OF_RESULTS/NUMBER_OF_THREADS),
                                   end_value=(1+k) * int(NUMBER_OF_RESULTS/NUMBER_OF_THREADS),
                                   file_handler=f)
            THREADS.append(thread)

        for thread in THREADS:
            thread.start()

        for thread in THREADS:
            thread.join()

        f.write("SENTINEL DATA\n")
        request = HTTP.request('GET', PYTHON_STRING.format(1))
        soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
        for link_href in soup.find_all('a'):
            data = link_href.get('href')
            if '?page=' in data:
                m = PYTHON_PAGE_REGEX.match(data)
                MAX_PAGE.append(int(m.groups()[0]))

        MAX_PAGE = max(MAX_PAGE)
        for x in range(1, MAX_PAGE+1):
            print("Page {0}".format(x))
            request = HTTP.request('GET', PYTHON_STRING.format(x))
            soup = BeautifulSoup(str(request.data, 'utf-8'), 'html.parser')
            for data in soup.find_all('a'):
                href = data.get('href')
                m = JOBS_BG_REGEX.match(href)
                if m:
                    full_href = "https://www.python.org" + href
                    f.write("{0} | {1}\n".format(data.string, full_href))
