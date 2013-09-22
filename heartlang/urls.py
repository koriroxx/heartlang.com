from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'heartlang.views.home'),
    url(r'^learn/', include('learn.urls')),
    url(r'^blog/$', include('blog.urls')),
	url(r'^profile/', include('users.urls')),
	url(r'^register/', 'heartlang.views.register'),
	#url(r'^login/', 'heartlang.views.login'),
	url(r'^logout/', 'heartlang.views.logout_page'), 
)

