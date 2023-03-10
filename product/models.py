from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100, verbose_name=_("name"))
    PRDCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("category"))
    PRDBBrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("brand"))
    PRDDescription = models.TextField(max_length=300, verbose_name=_("description"))
    PRDImage = models.ImageField(upload_to='product/', blank=True, null=True, verbose_name=_("image"),  default='default.jpg')
    PRDPrice = models.IntegerField(blank=True, null=True, verbose_name=_("price"))
    PRDDiscountprice = models.IntegerField(blank=True, null=True, verbose_name=_("Discountprice"))
    PRDCost = models.IntegerField(blank=True, null=True, verbose_name=_("cost"))
    PRDTime_created = models.DateTimeField(verbose_name=_("created"))
    
    PRDSlug = models.SlugField(blank=True, null=True, verbose_name=_("url"))
    PRDISNew = models.BooleanField(default=True, verbose_name=_("product is new"))
    PRDISBestSeller = models.BooleanField(default=False, verbose_name=_("product is best_saller"))


    def save(self, *args, **kwargs):
        self.PRDSlug = slugify(self.PRDName)
        super(Product,self).save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.PRDSlug})
        
        
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def __str__(self):
        return self.PRDName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    PRDIImage = models.ImageField(upload_to='product/', blank=True, null=True, verbose_name=_("image"))

    def __str__(self):
        return str(self.PRDIProduct)


class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_('Name'))
    CATParent = models.ForeignKey('self', limit_choices_to={'CATParent__isnull': True},
                                  verbose_name=_(' Main Category'), on_delete=models.CASCADE, blank=True, null=True)
    CATDescription = models.TextField(max_length=300, verbose_name=_('Description'), blank=True, null=True)
    CATImage = models.ImageField(upload_to='category', verbose_name=_('Image'), blank=True, null=True)

    def __str__(self):
        return self.CATName


class Product_Alternative(models.Model):
    PALTProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product', verbose_name=_('Product'))
    PALTAlternatives = models.ManyToManyField(Product, related_name='alternative_product', verbose_name=_('Alternatives'))

    class Meta:
        verbose_name = _('Product Alternative')
        verbose_name_plural = _('Product Alternatives')

    def __str__(self):
        return str(self.PALTProduct)


# Accessories
class Product_Accessory(models.Model):
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessory_product', verbose_name=_('Product'))
    PACCAccessories = models.ManyToManyField(Product, related_name='Accessory_product', verbose_name=_('Accessories'))

    class Meta:
        verbose_name = _('Product Accessory')
        verbose_name_plural = _('Product Accessories')

    def __str__(self):
        return str(self.PACCProduct)
