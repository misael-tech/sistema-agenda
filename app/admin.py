from django.contrib import admin
from .models import Servico,Agendamento

# Register your models here.

class ServicosAdmin(admin.ModelAdmin):
    ...

admin.site.register(Servico,ServicosAdmin)    


class AgendamentoAdmin(admin.ModelAdmin):
    ...

admin.site.register(Agendamento,AgendamentoAdmin)    