from django.db import models

# Create your models here.

class Trailer(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    link = models.URLField('Ссылка', help_text='Принимаются ссылки только с ютуб-хостинга')
    long_time = models.DecimalField("Длительность", max_digits=3,decimal_places=2)
    added = models.DateField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = 'Трейлер'
        verbose_name_plural = 'Трейлеры'
        ordering = ['-added']


class News(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    poster = models.ImageField('Постер')
    image = models.ImageField('Изображение')
    text = models.TextField("Текст")
    created = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

