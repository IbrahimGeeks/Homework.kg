from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Horse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя лошади')
    breed = models.CharField(max_length=100, verbose_name='Порода')
    age = models.IntegerField(verbose_name='Возраст')

    def __str__(self):
        return self.name
    
class Tourist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя туриста')
    horse = models.OneToOneField(Horse, on_delete=models.CASCADE, verbose_name='выбранная лошадь')

    def __str__(self):
        return f'{self.name} - {self.horse.name}'

class Review(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, verbose_name='Турист')
    company = models.ForeignKey('TourCompany', on_delete=models.CASCADE, related_name='company_reviews',verbose_name="Тур компания")
    text = models.TextField(verbose_name='Отзыв')
    stars = models.IntegerField(
        verbose_name="Оценка",
        validators=[
            MinValueValidator(1, message="Ошибка: оценка только от 1 до 5 (минимум 1)"),
            MaxValueValidator(5, message="Ошибка: оценка только от 1 до 5 (максимум 5)")
        ]
    )

    def __str__(self):
        return f"Отзыв от {self.tourist} для {self.company} — {self.stars} звёзд"
    
class TourCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название компании')
    description = models.TextField(verbose_name='Описание компании')

    def __str__(self):
        return self.name
    
class Service(models.Model):
    company = models.ManyToManyField(TourCompany, related_name='services', verbose_name='Компания')
    name = models.CharField(max_length=500, verbose_name='Название услуги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена услуги')

    def __str__(self):
        return f"{self.name} от {self.company.name} - {self.price} сом"
