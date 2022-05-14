from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField('Название', max_length=70, unique=True)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='films_image/')
    film = models.FileField('Фильм', upload_to='films/')
    age_control = models.CharField('Возрастное ограничение', max_length=5, help_text='MPAA система')
    rating_critic = models.DecimalField('Рейтинг критиков', max_digits=2, decimal_places=1)
    rating_viewer = models.DecimalField('Рейтинг зрителей', max_digits=2, decimal_places=1)
    relise_date = models.DateField("Дата выхода")
    # director_id = models.ManyToManyField()
    # actor_id = models.ManyToManyField()
    # genre_id = models.ManyToManyField()
    country = models.CharField("Страна", max_length=60)
    long_time = models.IntegerField("Длительность", max_length=3)