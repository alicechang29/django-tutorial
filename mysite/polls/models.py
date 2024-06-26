import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.


class Question(models.Model):
    # Model for a Question
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # Represents question as a string
        return self.question_text

    # use display decorator to customize the field
    # changed name from was published recently -> published recently?
    # set the order and made it checkmarks vs "True"
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        # returns T/F
        now = timezone.now()
        return (now - datetime.timedelta(days=1) <= self.pub_date <= now)


class Choice(models.Model):
    # Model for a Choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        # Represents choice as a string
        # Question.objects.all() --> outputs: <QuerySet [<Question: Hello>]>
        # instead of: <QuerySet [<Question: Question object (1)>]>
        return self.choice_text
