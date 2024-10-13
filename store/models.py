from django.db import models

class Customer(models.Model):
    email = models.EmailField(verbose_name="Email", unique=True)
    first_name = models.CharField(verbose_name="Имя",max_length=100)
    last_name = models.CharField(verbose_name="Фамилия",max_length=100)
    password = models.CharField(verbose_name="Пароль",max_length=100)

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
        ordering = ['-first_name']

    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(verbose_name="Название",max_length=100)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена",max_digits=8, decimal_places=2)
    image = models.ImageField(verbose_name="Изображение",upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(
        'Category',
        verbose_name ='Категория',
        blank = True,
        null=True,
        related_name='products',
        on_delete=models.SET_NULL,
    )
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(verbose_name="Название",max_length=100)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer= models.ForeignKey(
        'Customer',
        verbose_name='Покупатель',
        related_name='orders',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    address = models.ForeignKey(
        'Address',
        verbose_name='Адрес',
        related_name='orders',
        blank=True,
        on_delete=models.SET_NULL,
        null=True,
    )
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['created_at']

    def __str__(self):
        return f'Заказ для {self.customer}'


class Storage(models.Model):
    amount = models.PositiveIntegerField(verbose_name="Количество")
    price = models.PositiveIntegerField(verbose_name="Стоимость")
    product = models.OneToOneField(
        'Product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='storage',
        verbose_name='Продукт',
    )
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ['amount', 'price']

    def __str__(self):
        return f'{self.amount} {self.price}'


class Address(models.Model):
    street_address = models.CharField(verbose_name="Улица",max_length=100)
    city = models.CharField(verbose_name="Город",max_length=100, choices=(
        ('Уфа','Уфа'),
        ('Москва', 'Москва'),
    ))
    zipcode = models.IntegerField(verbose_name="Индекс",)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['street_address']

    def __str__(self):
        return f'{self.street_address}, {self.city}  {self.zipcode} '