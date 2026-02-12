from django.db import models

# Create your models here.


class Item(models.Model):

    name = models.CharField(max_length = 200)
    imagem = models.ImageField(upload_to='itens/', blank=True, null=True) 
    autor = models.CharField(max_length = 100)
    synopsis = models.CharField(max_length = 200)
    genre = models.CharField(max_length = 200)
    year = models.IntegerField(default=0)


    
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name