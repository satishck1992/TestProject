from django.shortcuts import render
from django.http import HttpResponse
from models import RedditIndia
from IPython import embed 
import json

def get_first_reddit_india_thread_link(request):
	response = {}
	try:
		response["link"] = RedditIndia().get_first_thread_link()
		response["status"] = 200
		response["message"] = "Success"
	except AttributeError:
		response["message"] = "Dom of reddit has changed"
		response["status"] = 400
	except Exception, e:
		response["message"] = "Internal Server Error"
		response["status"] = 500
	response = json.dumps(response)
	return HttpResponse(response)

def get_first_reddit_india_thread_html(request):
	response = {}
	try:
		response["html"] = RedditIndia().get_first_thread_html()
		response["status"] = 200
		response["message"] = "Success"
	except AttributeError:
		response["message"] = "Dom of reddit has changed"
		response["status"] = 400
	except Exception, e:
		response["message"] = "Internal Server Error"
		response["status"] = 500
	response = json.dumps(response)
	return HttpResponse(response)	