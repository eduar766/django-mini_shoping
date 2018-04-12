from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_stock = models.IntegerField(default=0)

    #Color Set
    YELLOW = 'YE'
    GREEN = 'GR'
    BLACK = 'BL'
    WHITE = "WH"
    COLOR_CHOICES = (
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLACK, 'Black'),
        (WHITE, 'White'),
    )

    color_name = models.CharField(
        max_length=50,
        choices = COLOR_CHOICES,
        default = BLACK,
    )

    #Weight set
    ONE_K = '1K'
    TWO_K = '2K'
    THREE_K = '3K'
    FOUR_K = "4K"
    WEIGHT_CHOICES = (
        (ONE_K, '1kg'),
        (TWO_K, '2kg'),
        (THREE_K, '3kg'),
        (FOUR_K, '4kg'),
    )

    weight_name = models.CharField(
        max_length=50,
        choices = WEIGHT_CHOICES,
        default = ONE_K,
    )

    description = models.TextField(null=True)
    def __str__(self):
        return self.product_name
