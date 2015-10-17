import unittest 
import requests

class RedditIndiaTestCase(unittest.TestCase):
	"""
	Relevant test scenarios for reddit scrapping
	"""
	def setUp(self):
		self.url = "http://localhost:8000"

	def test_get_first_thread_url(self):
		import json
		from django.core.exceptions import ValidationError
		from django.core.validators import URLValidator

		endpoint = self.url.strip() + "/reddit/india/first_thread_link"
		response = requests.get(endpoint)

		info = json.loads(response.content)

		assert info["status"] == 200

		validator = URLValidator()
		try:
			validator(info["link"])
		except ValidationError:
			assert False, "Not a valid URL"

	def test_get_first_thread_html(self):
		import json

		endpoint = self.url.strip() + "/reddit/india/first_thread_html"
		response = requests.get(endpoint)

		info = json.loads(response.content)

		assert info["status"] == 200

		validator(info["link"])


if __name__ == '__main__':  
    unittest.main() 