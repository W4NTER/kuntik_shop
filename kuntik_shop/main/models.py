from django.db import models

# Create your models here.


class UserPost(models.Model):
    color = models.CharField('Цвет', max_length=10)
    material = models.CharField('Материал', max_length=10)
    size = models.CharField('Размер', max_length=4)
    options = models.TextField('Дополнительные свойства', max_length=1000, default='None')


    # def __str__(self):
    #     return self.id

    # def get_absolute_url(self):
    #     return '/'

