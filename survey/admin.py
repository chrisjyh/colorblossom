from django.contrib import admin
from .models import Survey, Question, Choice, Result
# Register your models here.

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["survey", "question", "amount_choice", "use_yn"]
    list_filter = ["survey"]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = [ "question", "choice", "score"]
    list_filter = ["question"]

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["survey", "type"]