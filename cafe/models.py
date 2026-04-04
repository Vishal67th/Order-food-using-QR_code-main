from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class User(AbstractUser):
    email = None
    username = None
    phone = models.CharField(max_length=10, unique=True)
    phone_verified = models.BooleanField(default=False)
    cafe_manager = models.BooleanField(default=False)
    order_count = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone})"


class menu_item(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=250)
    pic = models.ImageField(upload_to='fimage')
    price = models.CharField(max_length=4, default='0')
    list_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['list_order', 'name']


class rating(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=250)
    r_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s review"

    class Meta:
        ordering = ['-r_date']


class order(models.Model):
    """
    ✅ Order model - KEPT ORIGINAL STRUCTURE
    Only added for compatibility, no new fields
    """
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=10, default='')
    table = models.CharField(max_length=15, default='take away')
    price = models.CharField(max_length=5, default='0')
    order_time = models.DateTimeField(auto_now_add=True)
    bill_clear = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.order_id} - {self.name} (Table: {self.table})"

    class Meta:
        ordering = ['-order_time']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class bill(models.Model):
    """
    Bill model - KEPT ORIGINAL STRUCTURE
    """
    order_items = models.CharField(max_length=5000)
    name = models.CharField(default='', max_length=50)
    bill_total = models.IntegerField()
    phone = models.CharField(max_length=10)
    bill_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bill - {self.name} (₹{self.bill_total})"

    class Meta:
        ordering = ['-bill_time']
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'