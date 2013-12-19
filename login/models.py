from django.db import models

# Create your models here.

class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length = 128)

class User(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 128)
    sec_question = models.ForeignKey(SecurityQuestion)
    sec_question_answer = models.CharField(max_length = 128)
