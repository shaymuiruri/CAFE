from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('Beverages', 'Beverages'),
        ('Snacks', 'Snacks'),
        ('Desserts', 'Desserts'),
        ('Meals', 'Meals')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name