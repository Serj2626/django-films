from django.db import models


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=50)
    description = models.TextField('Описание', blank=True)
    url = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Direction(models.Model):
    name = models.CharField('Фамилия и имя', max_length=150)
    description = models.TextField('Биография', blank=True)
    image = models.ImageField('Фотография', upload_to='image/directions/%Y')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Film(models.Model):
    '''Информация о фильме'''
    title = models.CharField('Название фильма', max_length=100)
    image = models.ImageField('Постер', upload_to='image/%Y')
    description = models.TextField('Описание', blank=True)
    date_publ = models.DateField('Дата выхода')
    directions = models.ManyToManyField(Direction, verbose_name='Режиссер')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
