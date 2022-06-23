from django.db import models

# Create your models here.
from PIL import Image



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
    actors = models.ManyToManyField(Celebrity, verbose_name='Актёр', related_name='actor_films', blank=True)
    directors = models.ManyToManyField(Celebrity, verbose_name='Директор', related_name='director_films', blank=True)
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

class FilmsPhoto(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to ='photos/')

    def save(self, *args, **kwargs):
        super(FilmsPhoto, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 1125 or img.width > 1125:
            img.thumbnail((1125, 1125))
        img.save(self.photo.path, quality=70, optimize=True)

    class Meta:
        verbose_name = 'Кадр с фильма'
        verbose_name_plural = 'Кадры с фильма'



class Comment(models.Model):
    author = models.ForeignKey('accounts.User',on_delete=models.CASCADE, related_name='film_comment_author')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film_comments')
    text = models.CharField('Текст', max_length=1200,)
    created = models.DateTimeField('Дата создания',auto_now_add=True)
    updated = models.DateTimeField('Дата обновления',auto_now=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created']

        def __str__(self):
            return str(self.text)[:60]


class RatingStar(models.Model):
    value = models.IntegerField('Значение')

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']

    def __str__(self):
            return f"{self.value}"

class Rating(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_rating')
    stars = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='film_rating')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        ordering = ['-created']

    def __str__(self):
        return f'{self.film} - {self.stars}'





