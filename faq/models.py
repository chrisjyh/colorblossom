from datetime import datetime

from django.db import models

# Create your models here.
class Faq(models.Model):
    title = models.CharField(max_length=500)
    answer = models.TextField()
    useyn = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AskInformation(models.Model):

    class Status(models.TextChoices):
        PAYMENT = "p", "결제/예약"
        SOLD_OUT = "A", "상담"
        ETC = "E", "기타"

    def get_response_yn(self):
        if self.respond_content != "":
            return "o"
        else:
            return "x"

    id = models.AutoField(primary_key=True)
    status = models.CharField(choices=Status.choices, default=Status.ETC, max_length=1)
    title = models.CharField(max_length=500, null=False, default="제목 없음")
    content = models.TextField(default="")
    respond_content = models.TextField(default="")
    reg_date = models.DateField(default=datetime.now)
    use_yn = models.BooleanField(default=True)

    def __str__(self):
        return self.title
