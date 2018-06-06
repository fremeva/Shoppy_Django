from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=250)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name