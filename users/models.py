from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    education = models.CharField(max_length=200, verbose_name="Образование")
    experience_years = models.PositiveIntegerField(default=0, verbose_name="Стаж (лет)")
    desired_salary = models.PositiveIntegerField(null=True, verbose_name="Ожидаемая ЗП")
    skills = models.TextField(verbose_name="Навыки")
    gender = models.CharField(max_length=10, choices=[('M', 'Муж'), ('F', 'Жен')], verbose_name="Пол")
    
    resume_file = models.FileField(upload_to='resumes/', verbose_name="Файл резюме")
    portfolio_image = models.ImageField(upload_to='portfolio/', verbose_name="Фото портфолио")

    def __str__(self):
        return f"{self.username} ({self.email})"