from tabnanny import verbose
from django.db import models
from django.forms import CharField

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name='description')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='image')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='price')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='discount %')
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='category')


    class Meta:
        db_table = 'product'
        verbose_name = 'product'
        verbose_name_plural = 'product'

    def __str__(self) -> str:
        return f'{self.name} quantity - {self.quantity}'
