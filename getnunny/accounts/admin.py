from django.contrib import admin

# Register your models here.
from .models import Nunny
from .models import HouseOwner
from .models import Order
from .models import Tag

admin.site.register(Nunny)
admin.site.register(HouseOwner)
admin.site.register(Order)
admin.site.register(Tag)