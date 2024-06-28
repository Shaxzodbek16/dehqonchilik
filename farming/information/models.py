from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='products/%Y/%m/%d/')
    category = models.ManyToManyField(Category, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'Products'


class Store(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField()
    photo = models.ImageField(upload_to='store/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'
        db_table = 'Store'


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'News'
        verbose_name = 'News'
        db_table = 'News'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    telephone = models.CharField(max_length=100)
    purpose = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}dan {self.text} {self.purpose} uchun, {self.telephone} raqami."

    class Meta:
        verbose_name_plural = 'Contact'
        verbose_name = 'Contact'
        ordering = ['created_at']
        db_table = 'Contact'
