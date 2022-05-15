from django.db import models

# Create your models here.


class Actor(models.Model):
    name = models.CharField('Имя', max_length=70)
    age = models.IntegerField('Возраст')
    is_alive = models.BooleanField('Жив', default=True)
    biography = models.TextField('Биография')
    image = models.ImageField('Фото', upload_to='actors_image/' )

    class Meta:
        verbose_name = "Актер"
        verbose_name_plural = "Актеры"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField('Имя', max_length=70)
    age = models.IntegerField('Возраст')
    is_alive = models.BooleanField('Жив', default=True)
    biography = models.TextField('Биография')
    image = models.ImageField('Фото', upload_to='director_image/')

    class Meta:
        verbose_name = "Режиссер"
        verbose_name_plural = "Режиссеры"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=30, unique=True)
    slug = models.SlugField('Слаг', max_length=50, unique=True)



    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ["name"]

    def __str__(self):
        return self.name




class Film(models.Model):
    name = models.CharField('Название', max_length=70)
    description = models.TextField('Описание')
    image = models.ImageField('Фото', upload_to='films_image/')
    film = models.FileField('Фильм', upload_to='films/')
    age_control = models.CharField('Возрастное ограничение', max_length=5, help_text='MPAA система')
    rating_critic = models.DecimalField('Рейтинг критиков', max_digits=3, decimal_places=1)
    rating_viewer = models.DecimalField('Рейтинг зрителей', max_digits=3, decimal_places=1)
    relise_date = models.CharField("Дата выхода", max_length=50)
    directors = models.ManyToManyField(Director,verbose_name='Режиссер',related_name='film_director')
    actors = models.ManyToManyField(Actor,verbose_name='Актер',related_name='film_actor')
    genres = models.ManyToManyField(Genre,verbose_name='Жанр',related_name='film_genre')
    country = models.CharField("Страна", max_length=60)
    long_time = models.IntegerField("Длительность")





