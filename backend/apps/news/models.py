from django.db import models
from backend.apps.accounts.models import User

# Create your models here.

class Trailer(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    link = models.URLField('Ссылка', help_text='Принимаются ссылки только с ютуб-хостинга')
    long_time = models.DecimalField("Длительность", max_digits=3, decimal_places=2)
    added = models.DateField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = 'Трейлер'
        verbose_name_plural = 'Трейлеры'
        ordering = ['-added']

    def __str__(self):
        return self.title


class NewsTag(models.Model):
    name = models.CharField('Название тэга', max_length=20)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField('Заголовок', max_length=60)
    poster = models.ImageField('Постер')
    image = models.ImageField('Изображение')
    tags = models.ManyToManyField(NewsTag, related_name='tag_news', blank=True)
    text = models.TextField("Текст")
    created = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_comment_author')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news_comments')
    text = models.CharField('Текст', max_length=1200,)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']

    def __str__(self):
        return str(self.text)[:60]

