from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display=('customer_name',)

admin.site.register(models.customers, CustomerAdmin)