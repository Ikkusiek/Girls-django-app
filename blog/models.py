from django.db import models                    #girlspower
from django.utils import timezone               #girlspower

class Post(models.Model):                          #(model.Model) oznacza, że ta klasa jest modelem django i powinien go przechowywać w bazie danych
    author = models.ForeignKey('auth.User')         #odnośnik do innego modelu
    title = models.CharField(max_length=200)       #tekst o ograniczonej liczbie znaków
    text = models.TextField()                       #tekst np artykuł o nieograniczonej ilości znaków
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def opublikuj(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title