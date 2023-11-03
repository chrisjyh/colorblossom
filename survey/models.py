import logging

from django.db import models
from accounts.models import User
from typing import List

logger = logging.getLogger(__name__)

# Create your models here.
class Survey(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    use_yn = models.CharField(max_length=1, default='y')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-reg_date']
        db_table = 'survey'
    
class Question(models.Model):
    uid = models.AutoField(primary_key=True)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE
    )
    question = models.TextField()
    amount_choice = models.TextField(default=0)
    use_yn = models.CharField(max_length=1, default='y')
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    uid = models.AutoField(primary_key=True)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.TextField()
    score = models.IntegerField(default=0)

class Result(models.Model):
    uid = models.AutoField(primary_key=True)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=500)
    explane = models.TextField()
    
class collect_result(models.Model):
    uid = models.AutoField(primary_key=True)
    survey = models.ForeignKey(
        Survey,
        on_delete=models.CASCADE
    )
    line_result = models.CharField(max_length= 500)
    body_result = models.CharField(max_length= 500)
    reg_date = models.DateTimeField(auto_now_add=True)