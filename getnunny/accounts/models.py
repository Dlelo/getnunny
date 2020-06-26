from django.db import models
# Create your models here.
class Nunny(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    tribe = models.CharField(max_length=100, null=True)
    language = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True)
    education = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=100, null=True)
    denomination = models.CharField(max_length=100, null=True)
    contact_person = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    pay_range = models.FloatField(null=True)
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
class HouseOwner(models.Model):
    CATEGORY=(
        ('LiveIn', 'LiveIn'),
        ('Dayburg','Dayburg'),
        ('Emmergency','Emergency' )

    )
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=100, null=True)
    denomination = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    contact_person = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('Queued for allocation','Queued for allocation'),
        ('Allocated','Allocated' )

    )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, null=True)
