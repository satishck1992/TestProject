from utils import get_soup
from IPython import embed

class RedditIndia():
	"""
	This class represents a RedditIndia instance.
	All the related methods like scrapping and getting 
	url and html will be provided with this class
	"""
	
	def __init__(self):
		self.url = "http://reddit.com/r/india"

	def get_first_thread_link(self):
		parsed_html = get_soup(self.url)
		comments_element = parsed_html.find('a', {"class": "comments"})
		comments_url = comments_element['href']
		return comments_url

	def get_first_thread_html(self):
		comments_url = self.get_first_thread_link()
		parsed_html = get_soup(comments_url)
		html_string = str(parsed_html)
		return html_string
