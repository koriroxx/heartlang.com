from django.db import models
from urllib import quote

from django.contrib.auth.models import User
import re



class Language(models.Model):
	title = models.CharField(max_length=100) 
	lessons = models.ManyToManyField('Lesson', related_name="learn_lesson_related", blank=True, null=True)
	games = models.ManyToManyField('Game', related_name="learn_game_related", blank=True, null=True)
	
	
	def get_lessons(self):
		return self.lesson_set.order_by("pk")
		

	def get_lesson_count(self):
		return self.lesson_set.count()
	
	def get_games(self):
		return self.game_set.order_by("pk")
	
	def __unicode__(self):
		return self.title
		
	def get_URL(self):
		return self.title
		
class Game(models.Model):
	title = models.CharField(max_length=100, blank=False, null=False)
	languages = models.ForeignKey(Language)
	URLTitle = models.CharField(max_length=100, blank=False, null=False)
	vocabulary_list = models.ManyToManyField('Vocabulary', related_name="game_vocabulary_related", blank=True, null=True)

	def get_game_vocab(self):
		return self.gamesvocabulary_set.order_by("english")

	def get_Script(self):
		return self.scriptURL
	
	def get_URL(self):
		return self.URLTitle
	
	def __unicode__(self):
		return self.title
		
class Vocabulary(models.Model):
	english = models.CharField(max_length=100, blank=False, null=False)
	translation = models.CharField(max_length=100, blank=False, null=False)
	game = models.ForeignKey(Game)
	usersvocabulary = models.ManyToManyField('UserVocabulary', related_name="vocabulary_uservocabulary_related", blank=True, null=True)
	
	def get_user_vocab(self):
		return self.usersvocabulary.order_by("vocabulary")
	
	def __unicode__(self):
		return self.english

class UserVocabulary(models.Model):
	vocabulary = models.ForeignKey(Vocabulary)
	strength = models.IntegerField(default=0)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.vocabulary.english
		
	def get_vocab(self):
		return self.vocabulary.english
	
class Lesson(models.Model):
	language = models.ForeignKey(Language)
	title = models.CharField(max_length=100, blank=True, null=True)
	pages = models.ManyToManyField('Page', related_name="learn_page_related", blank=True, null=True)
	URLTitle = models.CharField(max_length=100, blank=False, null=False)
	BEGINNER = 'B'
	INTERMEDIATE = 'I'
	ADVANCED = 'A'
	LEVEL_CHOICES = {
		(BEGINNER, 'Beginner'),
		(INTERMEDIATE, 'Intermediate'),
		(ADVANCED, 'Advanced')
	}
	level = models.CharField(max_length=1, choices=LEVEL_CHOICES)

	def get_pages(self):
		return self.page_set.order_by("title")

	def get_page_count(self):
		return self.page_set.count()

	def __unicode__(self):
		return self.title
		
	def get_URL(self):
		return self.URLTitle

class Page(models.Model):
	lesson = models.ForeignKey(Lesson)
	title = models.CharField(max_length=100)
	content = models.TextField()
	URLTitle = models.CharField(max_length=100, blank=False, null=False)
	pagenumber = models.IntegerField()

	def __unicode__(self):
		return self.title + ' "' + self.content[:20] + '" ... '

	def get_content(self):
		return self.content
		
	def get_URL(self):
		return self.URLTitle