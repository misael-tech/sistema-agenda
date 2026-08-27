from django.contrib import admin
from .models import Servico, Agendamento


@admin.register(Servico)
class ServicosAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "duracao",
    )

    search_fields = (
        "name",
        "descripiton",
    )

    ordering = (
        "name",
    )

    list_per_page = 20


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):

    list_display = (
        "nome",
        "telefone",
        "servico",
        "data",
        "horario",
        "metodo_pagamento",
    )

    search_fields = (
        "nome",
        "telefone",
    )

    list_filter = (
        "data",
        "metodo_pagamento",
        "servico",
    )

    ordering = (
        "-data",
        "horario",
    )

    list_per_page = 20

    date_hierarchy = "data"

    # Template personalizado dos agendamentos
    change_list_template = "admin/app/agendamento/change_list.html"