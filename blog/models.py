from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
'''
class Post(models.Model): — эта строка определяет нашу модель (объект).

class — это специальное ключевое слово для определения объектов.
Post — это имя модели.
models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных.
Дальше задаем свойства:
- author;
- title;
- text;
- created_date;
- published_date.

Чтобы это сделать, нужно определиться с типом полей (это текст? число? дата? ссылка на другой объект? например, на пользователя?).

models.ForeignKey — внешний ключ, ссылка на другую модель - AUTH_USER_MODEL.
models.CharField — текстовое поле с ограничением на количество символов.
models.TextField — поле для неограниченно длинного текста.
models.DateTimeField — дата и время.
'''