from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length = 50)
    b_id = models.IntegerField()

    def __str__(self):
        return self.name


class Branches(models.Model):
    ifsc = models.CharField(max_length = 20)
    bank = models.ForeignKey(Bank,related_name = "branches",on_delete = models.CASCADE)
    branch = models.CharField(max_length = 80)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    state = models.CharField(max_length = 26)

    def __str__(self):
        return self.ifsc