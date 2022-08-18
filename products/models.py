from django.db import models

from users.models import Profile

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=32)
    catDesc = models.CharField(max_length=128)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name


class manufacturer(models.Model):
    name = models.CharField(max_length=32)
    manDesc = models.CharField(max_length=128)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.name

class product(models.Model):
    title = models.CharField(max_length=32)
    proDesc = models.TextField(max_length=128)
    price = models.PositiveBigIntegerField()
    cat = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    man = models.ForeignKey(manufacturer, on_delete=models.DO_NOTHING)
    rating = models.PositiveSmallIntegerField()

    class Meta:
        app_label = 'products'

    def __str__(self):
        return self.title


class PurchaseRecord(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveSmallIntegerField()
    Bought_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'products'

    def __str__(self):
        return f'{self.product.name}{self.user.name}'