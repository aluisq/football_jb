from django.db import models

# Create your models here.

class Time(models.Model):
    
    time_id = models.AutoField(primary_key=True)
    nome_time = models.CharField(max_length=100)
    qt_max_jogador = models.IntegerField()
    qt_atual_jogador = models.IntegerField()
    num_titulo = models.IntegerField() 
    ativo = models.BooleanField()
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ['nome_time']
        db_table = 'time' # define your custom name

    def __str__(self):
        return f'{self.nome_time}'


class Campeonato(models.Model):

    campeonato_id = models.AutoField(primary_key=True) 
    edicao = models.IntegerField()
    data_termino = models.DateField()
    campeao = models.CharField(max_length=100, blank=True)
      
    class Meta:

        ordering = ['edicao']
        db_table = 'campeonato' # define your custom name

    def __str__(self):
        return f'{self.edicao}° Edição {self.campeao}'

class Resultado(models.Model):

    resultado_id = models.AutoField(primary_key=True) 
    equipe = models.ForeignKey(Time, on_delete= models.CASCADE)
    edicao = models.ForeignKey(Campeonato, on_delete = models.CASCADE)
    pontuacao = models.IntegerField()
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['pontuacao']
        db_table = 'resultado' # define your custom name

    def __str__(self):
        return f"{self.equipe} - {self.pontuacao} pontos" 