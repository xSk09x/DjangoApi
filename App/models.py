from django.db import models


class Plant(models.Model):
    text = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.text

# Create your models here.
