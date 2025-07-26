from django.db import models


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category')
    description = models.TextField(verbose_name='Short description')
    is_adult = models.BooleanField(default=False, verbose_name='Adult category (18+)')

    icon = models.FileField(upload_to='category_icons/', blank=True, null=True, verbose_name='Icon')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Question Category'
        verbose_name_plural = 'Question Categories'


class Question(models.Model):
    text = models.TextField(verbose_name='Question text')

    question_type = models.CharField(
        max_length=100,
        choices=[('truth', 'Truth'), ('dare', 'Dare')],
        verbose_name='Question type'
    )

    category = models.ForeignKey(
        QuestionCategory,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Category'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Rule(models.Model):
    text = models.TextField(verbose_name='Rule page content')
    order = models.PositiveIntegerField(default=0, verbose_name='Display order')

    class Meta:
        verbose_name = 'Rule Page'
        verbose_name_plural = 'Rule Pages'
        ordering = ['order']

    def __str__(self):
        return f'Page {self.order + 1}'
