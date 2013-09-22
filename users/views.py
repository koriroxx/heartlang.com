import re
from urllib import quote
from django.utils import timezone
from django.shortcuts import get_object_or_404, render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.template import RequestContext
from django.contrib.auth.models import User

from learn.models import Language, Lesson, Page
from users.models import Profile, Badges

@login_required()
def profile_home(Request, ProfileStr):
	
	if ProfileStr == None:
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
	
	else: 
		CurrProfile = get_object_or_404(User, username=ProfileStr)
		CurrProfile = Profile.objects.filter(user=CurrProfile)[0]
	
	return render_to_response('users/profile_home.html', {'user_name': CurrProfile }, context_instance=RequestContext(Request))
	
@login_required()
def badges_home(Request, ProfileStr):

	if ProfileStr == None:
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
	
	else: 
		CurrProfile = get_object_or_404(User, username=ProfileStr)
		CurrProfile = Profile.objects.filter(user=CurrProfile)[0]
	
	ProfileBadges = CurrProfile.get_badges()
	
	#If the language category already exists, don't show it again in template.
	PrevLang = ProfileBadges[0].language
	for badge in ProfileBadges:
		if badge.language == PrevLang:
			badge.haslang = False
		else:
			badge.haslang = True
			PrevLang = badge.language
	ProfileBadges[0].haslang = True
	
	return render_to_response('users/badges_home.html', {'user_name': CurrProfile, 'user_badges': ProfileBadges }, context_instance=RequestContext(Request))

@login_required()
def profile_language(Request, ProfileStr):

	if ProfileStr == None:
		CurrProfile = Profile.objects.filter(user=Request.user)[0]
	
	else: 
		CurrProfile = get_object_or_404(User, username=ProfileStr)
		CurrProfile = Profile.objects.filter(user=CurrProfile)[0]
	
	ProfileLanguages = CurrProfile.get_languages()
	
	
	return render_to_response('users/profile_languages.html', {'user_name': CurrProfile, 'user_languages': ProfileLanguages }, context_instance=RequestContext(Request))