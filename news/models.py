from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100, default='azzii')
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Статья - Введи текст')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
