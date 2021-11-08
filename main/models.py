from django.db import models
class a (models.Manager):
    pass
# Create your models here.

class Auto(models.Model):
    name = models.CharField(max_length=55, verbose_name='Марка авто')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена авто')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name='Модель авто')
    detail = models.ManyToManyField('Detail', verbose_name='Запчасти авто')
    objects = 'hello'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Product(models.Model):


    product_name =models.CharField(max_length=30)
    company_name =models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)


class Brand(models.Model):
    name = models.CharField(max_length=80, verbose_name='Модель авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'




class Detail(models.Model):
    name = models.CharField(max_length=80, verbose_name='Деталь авто')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'


