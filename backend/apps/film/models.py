from django.db import models

# Create your models here.




class Celebrity(models.Model):
    full_name = models.CharField('Имя', max_length=70)
    birthday = models.DateField("День рождения")
    country = models.CharField("Страна", max_length=60)
    is_alive = models.BooleanField('Жив', default=True)
    short_biography = models.TextField("Короткая биография")
    biography = models.TextField('Биография')
    career = models.CharField('Карьера', max_length=60)
    image = models.ImageField('Фото', upload_to='celebrity_image/')

    class Meta:
        verbose_name = "Знаменитость"
        verbose_name_plural = "Знаменитости"
        ordering = ["full_name"]

    def __str__(self):
        return self.full_name



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
    date_relise = models.DateField("Дата выхода")
    is_coming_soon = models.BooleanField("Это Анонс?", default=True)
    celebrities = models.ManyToManyField(Celebrity, verbose_name='Знаменитость', related_name='celebrity', blank=True)
    genres = models.ManyToManyField(Genre,verbose_name='Жанр',related_name='film_genre')
    country = models.CharField("Страна", max_length=60)
    long_time = models.IntegerField("Длительность")
    film_added = models.DateField("Фильм добавлен", auto_now_add=True)


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ["-film_added"]

    def __str__(self):
        return self.name[:15]










