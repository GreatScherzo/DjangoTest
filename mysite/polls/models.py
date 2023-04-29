import datetime

from django.db import models
from django.utils import timezone

## models yang dibuat utk poll app
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published bitch')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        Method utk tunjuk apadah kat shell api
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Create your models here.
