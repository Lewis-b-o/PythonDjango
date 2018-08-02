from django.db import models
from django.urls import reverse


"""module"""
# Create your models here.
# create category mode class


class Category(models.Model):

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    # meta class to pass in options to the model
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    # return a nice readable representation of the model
    def __str__(self):
        return '{}'.format(self.name)

# declare product model


class Product(models.Model):

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    # FK below, if any of the products are deleted, any reference in the category model are deleted with it.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # upload_to value product is were the images will be uploaded too and pulled from
    image = models.ImageField(upload_to='product', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('shop:proddetail', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)
