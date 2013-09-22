from django.contrib import admin
from learn.models import Language, Lesson, Page, Game, Vocabulary, UserVocabulary

admin.site.register(Language)
admin.site.register(Lesson)
admin.site.register(Page)
admin.site.register(Game)
admin.site.register(Vocabulary)
admin.site.register(UserVocabulary)