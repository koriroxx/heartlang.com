from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from learn.models import Language, Lesson, Page
from users.models import Profile, Badges
urlpatterns = patterns('users.views',
	url(r'^$', 'profile_home', {'ProfileStr': None}),
	url(r'^(?P<ProfileStr>[\w-]+)/$', 'profile_home'),
	url(r'^badges/$', 'badges_home', {'ProfileStr': None}),
	url(r'^(?P<ProfileStr>[\w-]+)/badges/$', 'badges_home'),
	url(r'^languages/$', 'profile_language', {'ProfileStr': None}),
	url(r'^(?P<ProfileStr>[\w-]+)/languages/$', 'profile_language'),
)

