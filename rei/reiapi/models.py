from django.db import models
from django.utils import timezone


class Question(models.Model):
    request_char = models.CharField('Request to cnn', max_length=500)
    answer_char = models.CharField('Answer rei', max_length=500)
    request_date = models.DateTimeField('Date created', default=timezone.now())

    def __str__(self):
        return self.request_char
