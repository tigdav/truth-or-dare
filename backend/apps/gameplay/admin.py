from django.contrib import admin
from .models import Question, QuestionCategory, Rule

admin.site.register(Question)
admin.site.register(QuestionCategory)
admin.site.register(Rule)
