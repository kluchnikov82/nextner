from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Product(models.Model):
    """
    Товар
    """

    food = 0
    non_food = 1

    FOOD_TYPES = (
        (food, 'Продовольственные'),
        (non_food, 'Не продовольственные'),
    )

    name = models.CharField(max_length=250,
                            db_index=True,
                            verbose_name='Наименование товара')
    type = models.IntegerField(choices=FOOD_TYPES, default=food)
    data_delivery = models.DateTimeField(null=True,
                                         verbose_name='Значение типа дата/время')
    points_of_issue = ArrayField(models.CharField(max_length=10, blank=True), size=8)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'PRODUCT'

    def __str__(self):
        return '%s -> %s' % (self.name, self.type)