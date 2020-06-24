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

    def _str_(self):
        return self.name
    
