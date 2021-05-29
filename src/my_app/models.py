from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100, db_index = True, verbose_name = 'Заголовок')
    slug = models.SlugField(max_length=100, unique=True, default=0.0)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('my_app:product_list_by_category', args=[self.slug])

class Size(models.Model):
    name = models.CharField(max_length=200, verbose_name='название', default=None)
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return f"{self.name}"

class Brand(models.Model):
    title = models.CharField(max_length = 100, db_index = True, verbose_name = 'Заголовок')
    slug = models.SlugField(max_length=100, unique=True, default=0.0)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('my_app:product_list_by_brand', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product', on_delete=models.CASCADE)
    title = models.TextField(max_length=100, db_index=True, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, db_index=True, unique=True, default=0.0)
    image = models.ImageField(upload_to='images', blank=True)
    body = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=100, decimal_places=1, default=0.0, verbose_name='Цена')
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    uploaded = models.DateField(auto_now=True)
    size = models.ManyToManyField(Size, max_length=20, verbose_name = 'размер')
    
    class Meta:
        ordering = ('title',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('my_app:product_detail', args=[self.id, self.slug])

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    customer_name = models.CharField(max_length=300, verbose_name='Имя')
    description = models.TextField(max_length = 1000, verbose_name='Описание')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.customer_name}"
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'