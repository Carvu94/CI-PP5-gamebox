from django.db import models
from django.contrib.auth.models import User

from products.models import Product
from profiles.models import UserProfile


class Review(models.Model):
    """
    Reviews model
    """
    author = models.ForeignKey(UserProfile,
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')
    content = models.TextField(max_length=1024)
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    def __str__(self):
        return '%s - %s' % (self.product.name, self.author)
