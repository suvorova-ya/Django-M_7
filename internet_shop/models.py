from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey("Staff", on_delete=models.CASCADE)

    products = models.ManyToManyField("Product", through='ProductOrder')

    def __str__(self):
        return str(self.time_in)


    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:  # если завершён, возвращаем разность объектов
            return (self.time_out - self.time_in).total_seconds()
        else:  # если ещё нет, то сколько длится выполнение
            return (datetime.now() - self.time_in).total_seconds()

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0, 'Quantity should be >= 0')])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name} {self.quantity}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/products/{self.id}'


class Category(models.Model):
    name = models.CharField(max_length=200)
    subscribers = models.ManyToManyField(User, through='SubscribersToCategory')

    def __str__(self):
        return f'{self.name}'

class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    _amount = models.IntegerField(default = 1, db_column = 'amount')

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = int(value) if value >= 0 else 0
        self.save()


class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик')
    ]
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()

    def __str__(self):
        return f'{self.full_name} {self.position}'


class Appointment(models.Model):
    date = models.DateField(default=datetime.utcnow,)
    user_name = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f'{self.user_name}: {self.message}'


class SubscribersToCategory(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return '{user}: {category}'.format(user=self.subscriber, category=self.categoryThrough)