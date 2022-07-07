from django.db import models

# Create your models here.


class category(models.Model):
    name = models.CharField(max_length=32)
    catDesc = models.CharField(max_length=128)


class manufacturer(models.Model):
    name = models.CharField(max_length=32)
    manDesc = models.CharField(max_length=128)


class product(models.Model):
    title = models.CharField(max_length=32)
    proDesc = models.TextField(max_length=128)
    price = models.PositiveSmallIntegerField()
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    man = models.ForeignKey(manufacturer, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
