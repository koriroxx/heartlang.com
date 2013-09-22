from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from learn.models import Language, Lesson, Game
from users.models import *
urlpatterns = patterns('learn.views',
    url(r'^$', 'learn_home'),
	url(r'^games/$', 'game_list'),
	url(r'^(?P<LanguageStr>[\w-]+)/$', 'language_home'),
	url(r'^(?P<LanguageStr>[\w-]+)/vocab/$', 'vocab_list'),
    url(r'^(?P<LanguageStr>[\w-]+)/lessons/$', 'lesson_list'),
	url(r'^(?P<LanguageStr>[\w-]+)/lessons/(?P<LessonURL>[\w-]+)/$', 'page_list'),
	url(r'^(?P<LanguageStr>[\w-]+)/lessons/(?P<LessonURL>[\w-]+)/(?P<PageURL>[\w-]+)/$', 'page_content'),
)

