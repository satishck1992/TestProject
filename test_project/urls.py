from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^reddit-thread/', 'test_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

)
