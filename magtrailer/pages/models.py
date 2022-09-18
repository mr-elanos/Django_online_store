from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Товар')
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.PositiveIntegerField(verbose_name='Залишок')
    available = models.BooleanField(default=True, verbose_name='Опубліковано')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створнення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    class Meta:
        ordering = ('price', 'name', 'category')
        indexes = [
            models.Index(fields=['id', 'slug'])
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    image = models.ImageField(upload_to='products_images/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('product', )
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return self.product
