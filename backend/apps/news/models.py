from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    image = models.ImageField('Фото', upload_to='news_image/')
    created = models.DateTimeField('Дата публикации', auto_now_add=True)



class Trailer(models.Model):
    title = models.CharField('Название',max_length=100)
    link = models.URLField('Сcылка', max_length=200)



