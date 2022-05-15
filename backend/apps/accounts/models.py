from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Rank(models.Model):
    name = models.CharField('Название', max_length=20)

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)
class User(AbstractUser):
    username = models.CharField("Имя пользователя", max_length=15)
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True)
    experience = models.IntegerField('Опыт', default=0)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    ranks = models.ManyToManyField(Rank, verbose_name='Ранг', related_name='user_rank')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

