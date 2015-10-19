from django.core.exceptions import ValidationError
import json
from django.core.validators import URLValidator
import unittest 
import requests
from IPython import embed

class RedditIndiaResponseTest(unittest.TestCase):
	"""
		Relevant functional test scenarios for reddit scrapping
	"""
	def setUp(self):
		self.url = "http://localhost:8000"

	def test_get_first_thread_link(self):
		endpoint = self.url.strip() + "/reddit_india/first_reddit_india_thread_link"
		response = requests.get(endpoint)

		info = json.loads(response.content)

		assert info["status"] == 200
		validator = URLValidator()
		try:
			validator(info["link"])
		except ValidationError:
			assert False, "Not a valid URL"

	def test_get_first_thread_html(self):

		endpoint = self.url.strip() + "/reddit_india/first_reddit_india_thread_html"
		response = requests.get(endpoint)
		info = json.loads(response.content)

		assert info["status"] == 200
		assert info["html"]


class RedditIndiaTest(unittest.TestCase):
	"""
		Unit Test scenarios for RedditIndia class
	"""
	
	def setUp(self):
		from models import RedditIndia
		self.reddit_india = RedditIndia()

	def test_get_first_thread_link(self):
		first_thread_link = self.reddit_india.get_first_thread_link()

		assert first_thread_link, "Dom of Reddit India Has Changed"
		validator = URLValidator()
		try:
			validator(first_thread_link)
		except ValidationError:
			assert False, "Not a valid URL"

	def test_get_first_thread_html(self):
		html = self.reddit_india.get_first_thread_html()
		assert html 

if __name__ == '__main__':  
    unittest.main() 