from django.contrib import admin

# Register your models here.
from healthappdata.models import Meds
from healthappdata.models import Order
from healthappdata.models import Transaction


admin.site.register(Meds)
admin.site.register(Order)
admin.site.register(Transaction)
