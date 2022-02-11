from django.utils import timezone
from django.db import models



class Category(models.Model):
    title = models.CharField('Категория товара', max_length=256)
    icon = models.ImageField('Иконка', upload_to='category_icons', blank=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField('Бренд товара', max_length=256)
    image = models.ImageField('Логотип', upload_to='product_logos', blank=True)


    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField('Цвет', max_length=256)


    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.title



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Бренд', related_name='brand_products')
    title = models.CharField('Название товара', max_length=256)
    text = models.TextField('Описание')
    year = models.IntegerField(default=0)
    image = models.ImageField('Фото', upload_to='product_image', blank=True)
    created_at = models.DateTimeField('Дата создания',default=timezone.now())
    color = models.ManyToManyField(Color, verbose_name='Цвет', through="ProductColor")



    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


    
class Memory(models.Model):
    size = models.IntegerField('Память', default=0)


    class Meta:
        verbose_name = 'Память'
        verbose_name_plural = 'Память'

    def __str__(self):
        return str(self.size)




class ProductColor(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет', related_name='color_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    size = models.ForeignKey(Memory, null=True,  on_delete=models.CASCADE, verbose_name='Память', related_name='memory_products')
    price = models.IntegerField('Цена', default=0)


    class Meta:
        verbose_name = 'Product color'
        verbose_name_plural = 'Product color'

    def __str__(self):
        return self.product.title + ' ' + self.color.title


class ProductGallery(models.Model):
    productColor = models.ForeignKey(ProductColor, on_delete=models.CASCADE, verbose_name='Продукт', related_name='gallery_products')
    image = models.ImageField('Фото продукта', upload_to='productColor gallery', blank=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.productColor.product.title