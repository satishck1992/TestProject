from django.conf.urls import patterns, include, url
from django.contrib import admin
import reddit_scraper
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^reddit_india/', 
    	include('reddit_scraper.urls')),
)
