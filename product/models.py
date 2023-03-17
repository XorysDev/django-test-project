from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
