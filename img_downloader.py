import urllib3
from urllib.error import HTTPError
import urllib.request
import time
import sys

from html.parser import HTMLParser

begin = int(time.time())

def utf8_to_url(string):
	string = string.split("/")
	good_source = ''.join(string[0:2]) + "/"
	for x in string[2:]:
		x = urllib.parse.quote(x)
		good_source = good_source + "/" + x

	return good_source

def end_stats():
	end = int(time.time())
	delta = end - begin

	write_lines_to_file()
	data = file_len(sys.argv[2])
	print("Time taken in seconds: " + str(delta))
	print( "Number of lines, aka visited pages: " + str(already_munched) )
	print("Pages per second: " + str(already_munched/delta))


def add_to_queve(url):
	queve.append(url)

def write_lines_to_file():
	with open(sys.argv[2], 'wb') as out:
		for entry in all_visited_links:
			entry += "\n"
			out.write(entry.encode('utf-8'))

	with open(sys.argv[3], 'wb') as out:
		for entry in all_visited_pictures:
			entry += "\n"
			out.write(entry.encode('utf-8'))
		

def file_len(fname):
	num_lines = sum(1 for line in open(fname))
	return num_lines

def add_to_visited(url):
	if url[0] == "#":
		all_visited_links[url] = 1
		return
	if global_url not in url:
		all_visited_links[url] = 1
		return
	all_visited_links[url] = 1
	add_to_queve(url)
	
def not_visited(url):
	if url not in all_visited_links:
		return True
	return False

def download_image(dest, source):
	global pictures_downloaded
	pictures_downloaded += 1
	good_source = utf8_to_url(source)
	try:
		urllib.request.urlretrieve(good_source, dest)
	except HTTPError as he:
		print("Unable to download image: " + good_source)
	except Exception as e:
		print("Unknown exception caught... " + e)

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == "img":
			for attribute in attrs:
				if attribute[0]=='src':
					global pictures_saw
					pictures_saw += 1
					fixed_url = attribute[1]
					if attribute[1][0:4] != "http":
						if not attribute[1][0] == '/':
							fixed_url = global_url + attribute[1]
						else:
							fixed_url = global_url + attribute[1][1:len(attribute[1])]

					#rename the url to where the image will be saved
					#because if it contains /, it's inside some directory
					#structure, so we relpace the / with |, as a rather rare symbol
					image_url = fixed_url.replace("/", "->")

					
					if image_url not in all_visited_pictures:
						all_visited_pictures[image_url] = 1
						download_image(dest = "data_downloaded/"+image_url, source = fixed_url)

		if tag == "a":
			for attribute in attrs:
				if attribute[0]=='href':
					fixed_url = attribute[1]
					if attribute[1][0:4] != "http":
						fixed_url = global_url + attribute[1][1:len(attribute[1])]
					if not_visited(url = fixed_url):
						add_to_visited(fixed_url)

parser = MyHTMLParser()

http = urllib3.PoolManager(num_pools=50)
global_url = sys.argv[1]

already_munched = 0
pictures_downloaded = 0
pictures_saw = 0
all_visited_links = {global_url: 1}
all_visited_pictures = {}
queve = [global_url]

try:
	while queve:
		already_munched += 1
		link = queve.pop(0)
		print("Now proccesing: "+link)
		
		try:
			parser.feed(str(http.request( 'GET', link ).data, 'utf-8'))
		except UnicodeDecodeError as ude:
			parser.feed(str(http.request( 'GET', link ).data, 'latin-1'))
		except UnicodeEncodeError as uee:
			parser.feed(str(http.request( 'GET', utf8_to_url(link) ).data, 'utf-8'))
			
		print("Number of links in the queve: {0}".format(len(queve)))
		print("Number of links proccessed: {0}".format(already_munched))
		print("Number of links seen: {0}".format(len(all_visited_links)))
		print("Images Downloaded/Images found: {0}/{1}".format(pictures_downloaded, pictures_saw))
		pictures_downloaded = 0
		pictures_saw = 0

except KeyboardInterrupt as key:
	end_stats()
else:
	end_stats()