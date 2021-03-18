from django.contrib import admin

from estrutura.models import Time, Campeonato, Resultado

# Registra o modelo no site
admin.site.register(Time)
admin.site.register(Campeonato)
admin.site.register(Resultado)

