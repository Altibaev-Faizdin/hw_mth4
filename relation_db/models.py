from django.db import models


class TouristCategory(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    photo = models.ImageField(
        upload_to='persons/',
        blank=True,
        null=True
    )

    categories = models.ManyToManyField(
        TouristCategory,
        blank=True,
        related_name='persons'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Tour(models.Model):
    title = models.CharField(
        max_length=150,
        default='Тур в горы'
    )
    description = models.TextField(
        default='Описание тура'
    )

    person = models.OneToOneField(
        Person,
        on_delete=models.CASCADE,
        related_name='tour'
    )

    def __str__(self):
        return f"{self.title} — {self.person}"



class Review(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.CharField(
        max_length=255,
        default='Отличный турист'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.person} | {self.text}"


