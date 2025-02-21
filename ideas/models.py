from django.db import models
from django.contrib.auth.models import User


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField("Дата создания", auto_now=True)
    title = models.CharField("Название", max_length=128)
    description = models.TextField("Описание")
    votes = models.IntegerField("Голоса", default=0)

    def __str__(self):
        return self.title
