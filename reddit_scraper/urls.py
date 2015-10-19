from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    url(r'^first_reddit_india_thread_link', 
    	views.get_first_reddit_india_thread_link, 
    	name='first_thread_url'),
    url(r'^first_reddit_india_thread_html', 
    	views.get_first_reddit_india_thread_html, 
    	name='first_thread_page'),
)
