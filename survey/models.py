import logging

from django.db import models
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
    pass

class Choice(models.Model):
    pass

class Result(models.Model):
    pass