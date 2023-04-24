from django.db import models


class Film(models.Model):
    '''Информация о фильме'''
    title = models.CharField(max_length=100)
    imag = models.ImageField(upload_to='image/%Y')
    description = models.TextField(blank=True)
    date_publ = models.DateField('Дата выхода')
