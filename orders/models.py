from django.db import models

# based on the which pizza option customer choose, different topping logic should be added.

# Create your models here.
class Regular_Pizza(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Sicilian_Pizza(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Toppings(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Subs(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Pasta(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Salads(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Dinner_Platters(models.Model):
    name = models.CharField(max_length=30)
    small = models.DecimalField(max_digits=100, decimal_places=2)
    large = models.DecimalField(max_digits=100, decimal_places=2)
    def __str__(self):
        return self.name

class Order(models.Model):
    menus = models.CharField(max_length=200)
    toppings = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=2000, decimal_places=2)
    def __str__(self):
        return self.menus