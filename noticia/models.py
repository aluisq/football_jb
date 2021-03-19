from django.db import models

# Create your models here.

class Noticia(models.Model):

    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['data_registro']
        db_table = 'noticia' # define your custom name
        verbose_name_plural = "Notícias"

    def __str__(self):
        return f'{self.nome_time}'