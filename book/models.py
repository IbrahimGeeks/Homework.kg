from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name='напишите название книги')
    description = models.TextField(verbose_name='напишите описание книги', blank=True)
    image = models.ImageField(upload_to='book/', verbose_name='загрузите изображение книги')
    book_file = models.FileField(upload_to='book/', verbose_name='загрузите файл книги')
    author = models.CharField(max_length=100, verbose_name='укажите автора книги', default='Неизвестен')
    price = models.PositiveIntegerField(verbose_name='укажите цену книги', default=0)
    pages = models.PositiveIntegerField(verbose_name='количество страниц', null=True, blank=True)
    published_year = models.IntegerField(verbose_name='год издания', null=True, blank=True)
    is_available = models.BooleanField(default=True, verbose_name='есть ли в наличии?')
    author_email = models.EmailField(verbose_name='email автора или издательства', blank=True)
    TYPE_BOOK = (
        ('программирование', 'программирование'),
        ('наука', 'наука'),
        ('искусство', 'искусство')
    )
    type_book = models.CharField(max_length=100,choices=TYPE_BOOK, verbose_name='выберите тип книги', default='программирование')
    created_at =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title