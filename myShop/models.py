from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100) 

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)  
    cost = models.PositiveIntegerField()       
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='items'  
    )

    def __str__(self):
        return self.title
