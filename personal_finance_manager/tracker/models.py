from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    
    CATEGORY_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.title} - {self.amount}"