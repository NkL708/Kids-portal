from django.db import models


class Article(models.Model):
    objects = models.Manager()
    
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст статьи',
        default='',
        blank=True
    )
    video_reference = models.CharField(
        max_length=150,
        verbose_name='Ссылка на видео',
        default='',
        blank=True,
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.title
