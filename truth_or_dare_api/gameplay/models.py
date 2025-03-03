from django.db import models


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_adult = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()

    question_type = models.CharField(
        max_length=100,
        choices=[('truth', 'Правда'), ('dare', 'Действие')]
    )

    categories = models.ManyToManyField(QuestionCategory, related_name='questions')

    def __str__(self):
        return self.text
