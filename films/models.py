from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Films(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название фильма')
    description = models.TextField(blank=True, null=True, verbose_name='Информация о фильме')
    category = models.CharField(max_length=250, verbose_name="Категория фильма")
    rating = models.IntegerField(verbose_name="Рейтинг фильма")
    url_film = models.URLField(blank=True, null=True, verbose_name='Ссылка на фильм')
    image = models.ImageField('Изображение', upload_to='img', null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return f'{self.name} - {self.category}'

