from django.db import models


class Googs(models.Model):

    title = models.CharField(verbose_name='Наименование',
                             max_length=255)
    created_at = models.DateTimeField(verbose_name='Дата поступления',
                                      auto_now_add=True,
                                      auto_created=True)
    price = models.DecimalField(verbose_name='Цена',
                                decimal_places=2,
                                max_digits=10)
    measurements = models.CharField(verbose_name='Единица измерения',
                                    max_length=25)
    vendor = models.CharField(verbose_name='Поставщик',
                              max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка товара'
        verbose_name_plural = 'Карточка товара'




