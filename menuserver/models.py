from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Dishes(models.Model):
    categary = models.CharField(max_length = 50)
    photo_url = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 200)
    price = models.FloatField()

    class Meta:
        verbose_name = 'dish'
        verbose_name_plural = 'dishes'

    def __str__(self):
        return self.name

class Stores(models.Model):
    store_id = models.CharField(max_length = 100, unique=True)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 500)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.name

class Roles(models.Model):
    # stores = models.ManyToManyField(Stores, through="storeManager", through_fields=('manager', 'store'))
    stores = models.ManyToManyField(Stores)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('C', 'Customer'),
        ('M', 'Manager'),
        ('E', 'Employee'),
    )
    role = models.CharField(max_length=1, choices=ROLES)

    class Meta:
            verbose_name = 'role'
            verbose_name_plural = 'roles'

    def __str__(self):
        return self.user.username

class Orders(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    num = models.IntegerField()
    is_submitted = models.BooleanField(default=False)
    username = models.CharField(max_length=50, default="anonymous")

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.username

class SubmittedOrders(models.Model):
    order = models.ManyToManyField(Orders)
    order_id = models.IntegerField()
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='Null')
    is_fulfill = models.BooleanField(default=False)
    is_decline = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'submittedorder'
        verbose_name_plural = 'submittedorders'

    def __str__(self):
        return str(self.order_id)
