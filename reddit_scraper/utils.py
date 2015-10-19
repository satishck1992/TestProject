from bs4 import BeautifulSoup
import requests

def get_soup(url):
	"""
		This functions gives the beautiful soup
		html tree of a webpage. 
		Which can be further processed to 
		extract relevant tags.
	""" 
	headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'
	}
	
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.content)
	return soup