from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Наименование предмета'
    )
    description = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(
        validators=[MinValueValidator(
            50, 'Число должно быть больше 49',
        )],
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name
