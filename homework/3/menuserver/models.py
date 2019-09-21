from django.db import models

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

class Managers(models.Model):
    # stores = models.ManyToManyField(Stores, through="storeManager", through_fields=('manager', 'store'))
    stores = models.ManyToManyField(Stores)
    name = models.CharField(max_length = 100)
    manager_id = models.CharField(max_length = 100, unique=True)

    class Meta:
        db_table = 'Manager'
        verbose_name = 'manager'
        verbose_name_plural = 'managers'

    def __str__(self):
        return self.name

class Employees(models.Model):
    stores = models.ManyToManyField(Stores)
    name = models.CharField(max_length = 100)
    employee_id = models.CharField(max_length = 100, unique=True)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name

class Orders(models.Model):
    dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    num = models.IntegerField()
    order_id = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return self.order_id

class SubmittedOrders(models.Model):
    order = models.ManyToManyField(Orders)
    order_id = models.IntegerField()
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='Null')
    is_fulfill = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'submittedorder'
        verbose_name_plural = 'submittedorders'

    def __str__(self):
        return str(self.order_id)

# class storeManager(models.Model):
#     store = models.ForeignKey(Stores, on_delete=models.CASCADE)
#     manager = models.ForeignKey(Managers, on_delete=models.CASCADE)
