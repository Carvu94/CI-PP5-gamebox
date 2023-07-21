from django.db import models


class Console(models.Model):
    # Consoles model
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    # Products model
    console = models.ForeignKey('Console',
                                null=True,
                                blank=True,
                                on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    genre = models.CharField(max_length=254)
    year = models.IntegerField()
    publisher = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
