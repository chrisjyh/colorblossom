from django.db import models

# Create your models here.
class Faq(models.Model):
    title = models.CharField(max_length=500)
    answer = models.TextField()
    useyn = models.BooleanField(default=True)

    def __str__(self):
        return self.title