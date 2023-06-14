from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    age = models.IntegerField()
    phone = models.CharField(max_length=150)
    email = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
