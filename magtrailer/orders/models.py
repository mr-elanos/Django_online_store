from django.db import models
from pages.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, verbose_name='Прізвище')
    clients_number = models.CharField(max_length=13, verbose_name='Телефонний номер')
    city = models.CharField(max_length=100, verbose_name="Місто")
    message = models.TextField(blank=True, verbose_name='Коментар до замовлення')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата задання')
    is_finished = models.BooleanField(default=False, verbose_name='Завершено / Не завершено')

    class Meta:
        ordering = ('date', 'is_finished', 'first_name')
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення № {self.id}, від {self.first_name} {self.last_name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Клієнт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
