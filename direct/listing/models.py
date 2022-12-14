from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.urls import reverse
from django.utils.timezone import now


class Listing(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=40,
    )
    overview = models.TextField(
        verbose_name='Описание'
    )
    big_image = models.ImageField(
        verbose_name='Большая картинка',
        upload_to = 'big/',
        default='static/img/listing/details/listing-hero.jpg',
    )
    med_image = models.ImageField(
        verbose_name='Средняя картинка',
        upload_to = 'med/',
        default ='static/img/listing/list-3.jpg',
    )
    small_image = models.ImageField(
        verbose_name='Маленькая картинка',
        upload_to = 'small/',
        default= 'static/img/listing/list_icon-3.png',
    )
    adress = models.CharField(
        verbose_name='Адресс',
        max_length= 40
    )
    phone = models.CharField(
        verbose_name='Телефон',
        max_length= 40
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=40
    )
    rating = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    coord = models.CharField(
        verbose_name='Координаты',
        max_length=40,
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )
    # Add site
    min_check = models.IntegerField(
        verbose_name='Минимальный чек',
        default=0,
    )
    max_check = models.IntegerField(
        verbose_name='Максимальный чек',
        default=100,
    )
    state = models.BooleanField(
        default=False,
        verbose_name='Открыто',
    )

    date_published = models.DateTimeField(
        default=now,
        verbose_name='date published'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing', kwargs={'listing_slug': self.slug})

    class Meta:
        db_table = 'listings'
        verbose_name = 'Листинг'
        verbose_name_plural = 'Листинги'
        ordering = ('date_published','rating','state','min_check','max_check',)


class Review(models.Model):

    text = models.TextField(
        verbose_name='Текст обзора',
        null=True
    )
    listing = models.ForeignKey(
        Listing,
        blank=True,
        on_delete=models.CASCADE,
    )
    is_published = models.BooleanField(
        verbose_name='Публикация',
        default=False,
    )
    date_published = models.DateTimeField(
        default=now,
        verbose_name='Дата публикации',
    )
    author = models.ForeignKey(
        'UserModel',
        blank=True,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг',
        default= 0,
        validators=[MinValueValidator(0),MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзоры'
        ordering = ('date_published','rating','listing',)

class UserModel(AbstractUser):
    avatar = models.ImageField(
        default= 'static/img/listing/details/comment.png',
        upload_to= 'avatar'
    )