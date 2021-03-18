from django.contrib import admin

from informativo.models import Gol, Cartao, Jogador

# Registra o modelo no site
admin.site.register(Gol)
admin.site.register(Cartao)
admin.site.register(Jogador)

