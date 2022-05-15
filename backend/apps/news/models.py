from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    text = models.TextField('Текст')
    image = models.ImageField('Фото', upload_to='news_image/')


