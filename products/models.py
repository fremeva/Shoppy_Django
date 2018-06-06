from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(blank=True, upload_to='products/')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', )