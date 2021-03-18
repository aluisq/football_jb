from django.db import models
from estrutura.models import Time

# Create your models here.

class Jogador(models.Model):
    
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    jogador_id = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=250)
    data_nascimento = models.DateField()
    foto_jogador = models.ImageField(upload_to='images/', blank=True) 
    cpf =  models.CharField(max_length=11, blank=True)
    contato = models.CharField(max_length=30, blank=True)
    ativo = models.BooleanField()
    data_registro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nome_completo']
        db_table = 'jogador' # define your custom name
        verbose_name_plural = "jogadores"

    def __str__(self):
        return f"{self.nome_completo}" 

class Gol(models.Model):

    GOLS= (
        ('H','Honra'),
        ('C','Contra')
    )

    gol_id = models.AutoField(primary_key=True)
    qt_gol = models.IntegerField()
    jogador = models.OneToOneField(Jogador, on_delete= models.CASCADE)
    tipo_gol = models.CharField(max_length=1, choices=GOLS)
    data_gol = models.DateField()

    class Meta:
        ordering = ['gol_id']
        db_table = 'gols' # define your custom name
        verbose_name_plural = "gols"
    
    def __str__(self):
        return f"{self.qt_gol} - {self.jogador}"

class Cartao(models.Model):

    CARTOES = (
        ('AMA', 'Amarelo'),
        ('AZL', 'Azul'),
        ('VRM', 'Vermelho'),
    )

    cartao_id = models.AutoField(primary_key=True)
    jogador = models.OneToOneField(Jogador, on_delete= models.CASCADE)
    qt_cartao = models.IntegerField()
    tipo_cartao = models.CharField(max_length=3, choices=CARTOES)
    data_cartao = models.DateField()

    class Meta:
        ordering = ['cartao_id']
        db_table = 'cartoes' # define your custom name
        verbose_name_plural = "cartões"
    
    def __str__(self):
        return f"{self.qt_cartao} {self.tipo_cartao} - {self.jogador} - {self.data_cartao}"

