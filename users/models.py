from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from learn.models import *

class Profile(models.Model):
	user = models.ForeignKey(User)
	badges = models.ManyToManyField('Badges', related_name='profile_badges_related', blank=True, null=True)
	current_languages = models.ManyToManyField(Language, related_name='profile_language_related', blank=True, null=True)
	vocabulary = models.ManyToManyField(UserVocabulary, related_name='profile_uservocabulary_related', blank=True, null=True)
	
	show_email = models.BooleanField(default=False)
	show_birthday = models.BooleanField(default=False)
	show_location = models.BooleanField(default=True)
	
	birthday = models.DateField(blank=False)
	location = models.CharField(max_length=100, blank=True, null=True)
	
	
	def __unicode__(self):
		return self.user.username
		
	def get_badges(self):
		return self.badges.order_by("language")
		
	def get_badges_count(self):
		return self.badges.count()
		
	def get_languages(self):
		return self.current_languages.order_by("title")
	
class Badges(models.Model):
	title = models.CharField(max_length=100)
	hearts = models.IntegerField()
	description = models.CharField(max_length=250)
	language = models.ForeignKey(Language)
	
	def __unicode__(self):
		return self.title