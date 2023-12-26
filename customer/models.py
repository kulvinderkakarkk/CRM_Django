from django.db import models
from django.contrib.auth.models import User

class customers(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=500)
    customer_email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name='customer')
