from django.db import models

# based on the which pizza option customer choose, different topping logic should be added.

# Create your models here.
class Regular_Pizza(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)


class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)


class Toppings(models.Model):
    name = models.CharField(max_length=30)


class Subs(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)


class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Salads:
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Dinner_Platters:
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)