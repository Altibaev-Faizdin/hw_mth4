from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    cover = models.ImageField(upload_to='book/', blank=True, verbose_name="Обложка книги")
    author = models.CharField(max_length=200, verbose_name="Автор книги")
    description = models.TextField(verbose_name="Описание книги")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Цена книги")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    published_date = models.DateField(verbose_name="Дата публикации")
    file = models.FileField(upload_to='book/', null=True, blank=True, verbose_name="Файл книги")
    website = models.URLField(null=True, blank=True, verbose_name="Сайт книги")
    email = models.EmailField(null=True, blank=True, verbose_name="Email для связи")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
