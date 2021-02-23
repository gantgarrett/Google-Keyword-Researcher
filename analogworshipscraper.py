import requests, os
from bs4 import BeautifulSoup

os.makedirs('analogworshipdiscog', exist_ok=True)

def get_images(url, max_pages=None):
	page = 1
	while not max_pages or page <= max_pages:
		print('Scraping page:', page)
		r = requests.get(url, params={'page': page})
		soup = BeautifulSoup(r.text, 'html.parser')
		imageElems = soup.select('.imageInnerContainer a')
		
		for imageElem in imageElems:
			imageUrl = 'https://www.analogworship.com' + imageElem.get('href')[0:]
			print('Downloading image %s...' % (imageUrl))
			res = requests.get(imageUrl)
			if res.ok:
				f = open(os.path.join('analogworshipdiscog', os.path.basename(imageUrl)), 'wb')
				for chunk in res.iter_content(100000):
					f.write(chunk)
				f.close()
		page += 1

url = 'https://www.analogworship.com'
get_images(url, max_pages=30)
