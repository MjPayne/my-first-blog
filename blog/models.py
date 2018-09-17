from django.db import models
from django.utils import timezone

class Post(models.Model):    #define o modelo 'é um objeto'. Post é o nome do objeto
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   #definição das propriedades
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now
    )
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #definição de função
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


