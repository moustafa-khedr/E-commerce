from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("product name"))
    # PRDCategory =
    PRDDescription = models.TextField(max_length=300, verbose_name=_("product description"))
    PRDPrice = models.IntegerField(blank=True, null=True, verbose_name=_("product price"))
    PRDCost = models.IntegerField(blank=True, null=True, verbose_name=_("product cost"))
    PRDTime_created = models.DateTimeField(verbose_name=_("product created"))
    # PRDImage =

    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    PRDIImage = models.ImageField(upload_to='product/', blank=True, null=True, verbose_name=_("image"))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50)
    CATParent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    CATDescription = models.TextField(max_length=300, blank=True, null=True)
    CATImage = models.ImageField(upload_to='category', blank=True, null=True)

    def __str__(self):
        return self.CATName



    # Alternatives
    # Accessories
