import requests
import os, os.path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

store = 'images'
if not os.path.exists(store):
    os.makedirs(store)

url = 'https://www.flickr.com/groups/735978@N21/pool/'
pages_to_scrape = 15

def download(url):
	r = requests.get(url, stream=True)
	filename = urlparse(url).path.split('/')[-1]
	print("Downloading to:", filename)
	with open(os.path.join(store, filename), 'wb') as the_image:
		for byte_chunk in r.iter_content(chunk_size=4096*4):
			the_image.write(byte_chunk)