from datetime import date, datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from .models import Servico, Agendamento


HORARIOS_ATENDIMENTO = [
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    
]


def home(request):

    servicos = Servico.objects.all()

    return render(request, 'index.html', {
        'servicos': servicos
    })


def agendamento(request, servico_id):

    servico = get_object_or_404(Servico, id=servico_id)

    # =========================
    # GET
    # =========================

    if request.method == "GET":

        return render(request, 'agendamento.html', {
            'servico': servico,
            'horarios': HORARIOS_ATENDIMENTO,
            'hoje': date.today().isoformat()
        })


    # =========================
    # POST
    # =========================

    elif request.method == "POST":

        nome = request.POST.get("nome")
        telefone = request.POST.get("telefone")
        metodo_pagamento = request.POST.get("metodo_pagamento")
        data = request.POST.get("data")
        horario = request.POST.get("horario")


        # =========================
        # VALIDAR DATA
        # =========================

        try:
            data_agendamento = datetime.strptime(
                data,
                "%Y-%m-%d"
            ).date()

        except (ValueError, TypeError):

            return render(request, "agendamento.html", {
                "servico": servico,
                "horarios": HORARIOS_ATENDIMENTO,
                "hoje": date.today().isoformat(),
                "erro": "Data inválida."
            })


        # Não permite data passada

        if data_agendamento < date.today():

            return render(request, "agendamento.html", {
                "servico": servico,
                "horarios": HORARIOS_ATENDIMENTO,
                "hoje": date.today().isoformat(),
                "erro": "Não é possível agendar uma data passada."
            })


        # =========================
        # VALIDAR HORÁRIO
        # =========================

        if horario not in HORARIOS_ATENDIMENTO:

            return render(request, "agendamento.html", {
                "servico": servico,
                "horarios": HORARIOS_ATENDIMENTO,
                "hoje": date.today().isoformat(),
                "erro": "Horário inválido."
            })


        # =========================
        # VERIFICAR HORÁRIO PASSADO
        # =========================

        if data_agendamento == date.today():

            agora = datetime.now().time()

            horario_agendamento = datetime.strptime(
                horario,
                "%H:%M"
            ).time()

            if horario_agendamento <= agora:

                return render(request, "agendamento.html", {
                    "servico": servico,
                    "horarios": HORARIOS_ATENDIMENTO,
                    "hoje": date.today().isoformat(),
                    "erro": "Não é possível agendar um horário que já passou."
                })


        # =========================
        # VERIFICAR SE ESTÁ OCUPADO
        # =========================

        horario_ocupado = Agendamento.objects.filter(
            data=data_agendamento,
            horario=horario
        ).exists()


        if horario_ocupado:

            return render(request, "agendamento.html", {
                "servico": servico,
                "horarios": HORARIOS_ATENDIMENTO,
                "hoje": date.today().isoformat(),
                "erro": "Este horário já está ocupado. Escolha outro horário."
            })


        # =========================
        # CRIAR AGENDAMENTO
        # =========================

        agendamento = Agendamento.objects.create(
            servico=servico,
            nome=nome,
            telefone=telefone,
            metodo_pagamento=metodo_pagamento,
            data=data_agendamento,
            horario=horario
        )


        # =========================
        # REDIRECIONAR
        # =========================

        return redirect(
            "comprovante",
            agendamento_id=agendamento.id
        )


# =========================
# COMPROVANTE
# =========================

def comprovante(request, agendamento_id):

    agendamento = get_object_or_404(
        Agendamento,
        id=agendamento_id
    )

    return render(request, "comprovante.html", {
        "agendamento": agendamento
    })


# =========================
# HORÁRIOS DISPONÍVEIS - AJAX
# =========================

def horarios_disponiveis(request, servico_id):

    data = request.GET.get("data")


    if not data:

        return JsonResponse({
            "horarios_ocupados": []
        })


    horarios_ocupados = [
        horario.strftime("%H:%M")
        for horario in Agendamento.objects.filter(
            data=data
        ).values_list(
            "horario",
            flat=True
        )
    ]


    return JsonResponse({
        "horarios_ocupados": horarios_ocupados
    })