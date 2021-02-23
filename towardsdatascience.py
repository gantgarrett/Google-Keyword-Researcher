import requests
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = requests.get("https://tapeheadcity.com" + pageUrl)
	bsObj = BeautifulSoup(html)
	try:
		print(bsObj.h3.div.get_text())
	except AttributeError:
		print("This page is missing something! No worries though!")

	for link in bsObj.findAll("a", href=re.compile("^(/collections/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#We have encountered a new page
				newPage = link.attrs['href']
				print("----------------------\n"+newPage)
				pages.add(newPage)
				getLinks(newpage)
getLinks("")