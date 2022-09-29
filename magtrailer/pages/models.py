from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to='products_images/%Y/%m/%d', blank=True, null=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('all_categories', kwargs={'cat_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Товар')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(verbose_name='Залишок')
    available = models.BooleanField(default=True, verbose_name='Опубліковано')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створнення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    availability = models.CharField(max_length=30, verbose_name='Наявність')
    width = models.IntegerField(verbose_name='Ширина кузова')
    length = models.IntegerField(verbose_name='Довжина кузова')
    height = models.IntegerField(verbose_name='Висота борту')
    full_weight = models.IntegerField(verbose_name='Повна маса')
    max_weight = models.IntegerField(verbose_name="Вантажопід'ємність")
    image = models.ImageField(upload_to='products_images/%Y/%m/%d', blank=True, null=True)

    class Meta:
        ordering = ('price', 'name', 'category')
        indexes = [
            models.Index(fields=['id', 'slug'])
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='products_images/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('product', )
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return f'{self.product}'


class Contacts(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Ім'я")
    last_name = models.CharField(max_length=30, verbose_name='Прізвище')
    clients_number = models.CharField(max_length=13, verbose_name='Телефонний номер')
    message = models.TextField(verbose_name='Питання')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата задання')
    is_answer = models.BooleanField(default=False, verbose_name='Прочитано / Не прочитано')

    class Meta:
        ordering = ('date', 'is_answer', 'first_name')
        verbose_name = 'Запитання'
        verbose_name_plural = 'Запитання'

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
