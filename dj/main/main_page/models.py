from django.db import models
from datetime import date

class Category(models.Model): # Модель таблицы Категорий
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model): # Модель таблицы Подкатегорий
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name

class Status(models.Model): # Модель таблицы Статусов
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Type_cashflow(models.Model): # Модель таблицы Типов
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Cashflow(models.Model): # Модель таблицы Записей
    date_create = models.DateField(default=date.today)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)  # Исправлено
    type_cashflow = models.ForeignKey(Type_cashflow, on_delete=models.SET_NULL, null=True)  # Исправлено
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    sum_cashflow = models.IntegerField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.date_create} - {self.status} - {self.type_cashflow} - {self.sum_cashflow}"
