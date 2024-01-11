from django.db import models


# Create your models here.

class Reservation(models.Model):
    class Status(models.TextChoices):
        PAYMENT = "PAYMENT", "예약금 입금"
        RESERVED = "RESERVED", "예약 완료"
        WAITTING = "WAITTING", "예약 대기"

    class BookCourse(models.TextChoices):
        SIMPLE = "SIMPLE", "간단 진단"
        BASIC = "BASIC", "기본 진단"
        BODY = "BODY", "골격 진단"
        PRO = "PRO", "프로 진단"

    id = models.AutoField(primary_key=True)
    status = models.CharField(choices=Status.choices, default=Status.WAITTING, max_length=50)
    course = models.CharField(choices=BookCourse.choices, default=BookCourse.SIMPLE, max_length=50)
    reservation_many = models.IntegerField(default=1)
    name = models.CharField(max_length=100, null=False, default="익명")
    email = models.EmailField(max_length=200, default="<Email>")
    phone = models.CharField(max_length=50, null=False, default="010-0000-0000")
    reservation_date = models.DateField(null=False)
    reservation_hour = models.BigIntegerField(null=False)
    reservation_min = models.BigIntegerField(null=False)
    reg_date = models.DateTimeField(auto_now=True)
    use_yn = models.BooleanField(default=True)

    def show_date_time(self):
        return f"{self.reservation_date} {self.reservation_hour}:{self.reservation_min} "

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = "예약 관리"


