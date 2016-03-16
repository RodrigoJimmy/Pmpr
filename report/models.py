from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"


class Location(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Incident(models.Model):
    organization = models.CharField(max_length=32)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL, null=True)
    caller = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=200)
    num = models.IntegerField()
    date_time = models.DateTimeField()
    result = models.CharField(max_length=64)
    doc = models.CharField(max_length=12)

    def __str__(self):
        return self.category.name
