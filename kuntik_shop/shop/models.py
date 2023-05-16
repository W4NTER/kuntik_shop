from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField('Название', max_length=30)
    color = models.CharField('Цвет', max_length=10)
    material = models.CharField('Материал', max_length=10)
    size = models.CharField('Размер', max_length=4)
    weight = models.CharField('Масса', max_length=3)
    photo = models.ImageField('Фото', default="None", upload_to="photos")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица производителя'