import re
from urllib import quote
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext

from learn.models import Language, Lesson, Page, Game, Vocabulary, UserVocabulary
from users.models import Profile, Badges

def learn_home(Request):
	CurrProfile = None
	ProfileBadges = None
	totalhearts = 0
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts
		

	Languages = Language.objects.order_by("pk")
	return render_to_response('learn/learn.html', {'language_list': Languages, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))
	
def language_home(Request, LanguageStr):
	CurrProfile = None
	ProfileBadges = None
	totalhearts = 0
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts

	CurrLanguage = get_object_or_404(Language, title=LanguageStr)
	Lessons = CurrLanguage.get_lessons()
	Games = CurrLanguage.get_games()
	Title = CurrLanguage.title
		
	#add game list
	return render_to_response('learn/language_home.html', {'lesson_list': Lessons, 'language_title': Title, 'game_list': Games, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))

def game_list(Request):
	Languages = Language.objects.order_by("pk")
	return render_to_response('learn/game.html', {'language_list': Languages}, context_instance=RequestContext(Request))

def vocab_list(Request, LanguageStr):
	CurrLanguage = get_object_or_404(Language, title=LanguageStr)
	CurrProfile = None
	ProfileBadges = None
	totalhearts = 0
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts
	
	try:
		VocabList = UserVocabulary.objects.filter(user=Request.user)[0]
	except UserVocabulary.DoesNotExist:
		raise Http404
	
	UserVocab = VocabList.vocabulary.get_user_vocab()
	
	return render_to_response('learn/vocablist.html', {'language': CurrLanguage, 'vocab_list': UserVocab, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))

	
def lesson_list(Request, LanguageStr):

	CurrProfile = None
	ProfileBadges = None
	totalhearts = 0
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts

	CurrLanguage = get_object_or_404(Language, title=LanguageStr)
	Lessons = CurrLanguage.get_lessons()
	Title = CurrLanguage.title


	return render_to_response('learn/lessons.html', {'lesson_list': Lessons, 'language_title': Title, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))
	
def page_list(Request, LanguageStr, LessonURL):
	CurrProfile = None
	ProfileBadges = None
	totalhearts = 0
	
	if Request.user.is_authenticated(): 
		#Set the current profile
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
			
		#Get the user's badge(s)
		ProfileBadges = CurrProfile.get_badges()
		totalhearts = 0;
		#Get the total amount of hearts a user has
		for badges in ProfileBadges:
			totalhearts += badges.hearts
	CurrLanguage = get_object_or_404(Language, title=LanguageStr)
	try:
		CurrLesson = Lesson.objects.get(URLTitle=LessonURL, language=CurrLanguage)
	except Lesson.DoesNotExist:
		raise Http404
	Pages = CurrLesson.get_pages()
	Title = CurrLesson.title
	
	
		
	return render_to_response('learn/pages.html', {'page_list': Pages, 'lesson_title': Title, 'badges_list': ProfileBadges, 'profile': CurrProfile, 'total_hearts': totalhearts}, context_instance=RequestContext(Request))


def page_content(Request, LanguageStr, LessonURL, PageURL):
	CurrLanguage = get_object_or_404(Language, title=LanguageStr)
	
	try:
		CurrLesson = Lesson.objects.get(URLTitle=LessonURL, language=CurrLanguage)
	except Lesson.DoesNotExist:
		raise Http404
	
	
	try:
		CurrPage = Page.objects.get(URLTitle=PageURL, lesson=CurrLesson)
	except Page.DoesNotExist:
		raise Http404
		
	Title = CurrLesson.title
	NextPage = None
	PrevPage = None
	
	try:
		if CurrPage.pagenumber < CurrLesson.get_page_count():
			NextPage = Page.objects.get(lesson=CurrLesson, pagenumber=CurrPage.pagenumber+1)
	except Page.DoesNotExist:
		pass
		
	try:
		if CurrPage.pagenumber != 0:
			PrevPage = Page.objects.get(lesson=CurrLesson, pagenumber=CurrPage.pagenumber-1)
	except Page.DoesNotExist:
		pass
	
	return render_to_response('learn/currpage.html', {'page_content': CurrPage, 'lesson_title': Title, 'next_page': NextPage, 'prev_page': PrevPage}, context_instance=RequestContext(Request))
