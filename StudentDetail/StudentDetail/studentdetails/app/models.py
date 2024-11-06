from django.db import models

# Create your models here.


class details(models.Model):
    name = models.CharField(max_length=100)
    college_id = models.BigIntegerField()
    email = models.EmailField()
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    branch = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
