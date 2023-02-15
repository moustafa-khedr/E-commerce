from django.db import models


# Create your models here.


class Product(models.Model):
    PRDName = models.CharField(max_length=100)
    # PRDCategory =
    PRDDescription = models.TextField(max_length=300)
    PRDPrice = models.IntegerField(blank=True, null=True)
    PRDCost = models.IntegerField(blank=True, null=True)
    PRDTime_created = models.DateTimeField()
    # PRDImage =

    def __str__(self):
        return self.PRDName

    # category
    # Images
    # Alternatives
    # Accessories
