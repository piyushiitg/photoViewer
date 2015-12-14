from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^test', 'photoviewer.views.testing'),
	url(r'^uploadfile', 'photoviewer.views.uploadfile'),
	)

