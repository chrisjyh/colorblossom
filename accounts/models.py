from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.db.models import SET_NULL

from base import settings


# Create your models here.
# 커스텀 유저모델을 위해 기존 유저모델 상속 자세한내용을 원하면 AbstractUser 컨트롤 클릭
class User(AbstractUser):
    pass


class PersonalColor(models.TextChoices):
    SPRINGBRIGHT = "SPRINGBRIGHT", "봄 브라이트"
    SPRINGTRUE = "SPRINGTRUE", "봄 트루"
    SUMMERBRIGHT = "SUMMERBRIGHT", "여름 브라이트"
    SUMMERMUTE = "SUMMERMUTE", "여름 트루"
    FALLBRIGHT = "FALLBRIGHT", "가을 브라이트"
    FALLTRUE = "FALLTRUE", "가을 트루"
    FALLDEEP = "FALLDEEP", "가을 딥"
    WINTERBRIGHT = "WINTERBRIGHT", "겨울 브라이트"
    WINTERDEEP = "WINTERDEEP", "겨울 딥"


class RecommendMarkup(models.Model):
    type = models.CharField(choices=PersonalColor.choices, default=PersonalColor.SPRINGBRIGHT, max_length=50)
    content = models.TextField()
    link = models.URLField(blank=True)
    class Meta:
        verbose_name = verbose_name_plural = "화장품추천"


class ReservationUser(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    consultResult = models.CharField(choices=PersonalColor.choices, null=True, max_length=50)
    consultResult02 = models.CharField(choices=PersonalColor.choices, null=True, max_length=50)
    reg_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = verbose_name_plural = "회원관리"
