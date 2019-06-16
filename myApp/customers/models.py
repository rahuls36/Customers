from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 200)
    dob = models.DateField(max_length = 8)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name