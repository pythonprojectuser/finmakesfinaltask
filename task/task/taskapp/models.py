from django.db import models


class UserModel(models.Model):
    name=models.CharField(max_length=250)
    age = models.CharField(max_length=250)
    dob = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    course = models.CharField(max_length=250)

    def __str__(self):
        return self.name