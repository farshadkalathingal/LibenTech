from django.db import models

# Create your models here.
class Demo(models.Model):
    name = models.CharField(max_length=120)
    bar_value = models.IntegerField()
    d_allocated = models.IntegerField()
    d_available = models.IntegerField()
    f_paid = models.IntegerField()
    f_open = models.IntegerField()