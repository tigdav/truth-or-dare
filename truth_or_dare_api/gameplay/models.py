from django.db import models


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Краткое описание')
    is_adult = models.BooleanField(default=False, verbose_name='Категория для взрослых (18+)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория вопроса'
        verbose_name_plural = 'Категории вопросов'


class Question(models.Model):
    text = models.TextField(verbose_name='Содержание вопроса')

    question_type = models.CharField(
        max_length=100,
        choices=[('truth', 'Правда'), ('dare', 'Действие')],
        verbose_name='Тип вопроса'
    )

    category = models.ForeignKey(
        QuestionCategory,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Категория вопроса'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
