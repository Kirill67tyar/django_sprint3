import datetime as dt

from django.db import models
from django.contrib.auth import get_user_model

from blog.utils import output_for_model


User = get_user_model()
MAX_LENGTH = 256


class PublishedWithTimeStampModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
    )

    class Meta:
        abstract = True


class ValidPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            pub_date__lte=dt.datetime.now(),
            is_published=True,
            category__is_published=True,
        ).select_related('location', 'author', 'category',)


class Post(PublishedWithTimeStampModel):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Заголовок',
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text=(
            'Если установить дату и время в будущем'
            ' — можно делать отложенные публикации.'
        )
    )
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )
    location = models.ForeignKey(
        to='blog.Location',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        to='blog.Category',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )

    objects = models.Manager()
    valid_posts = ValidPostsManager()

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('pub_date', 'title',)
        default_related_name = 'posts'

    def __str__(self):
        return output_for_model(self.title)


class Category(PublishedWithTimeStampModel):
    title = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Заголовок',
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text=(
            'Идентификатор страницы для URL; разрешены'
            ' символы латиницы, цифры, дефис и подчёркивание.'
        )
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return output_for_model(self.title)


class Location(PublishedWithTimeStampModel):
    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name='Название места',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return output_for_model(self.name)
