from django.contrib import admin
from django.urls import path

from app import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'agendamento/<int:servico_id>/',
        views.agendamento,
        name='agenda'
    ),

    path(
        'comprovante/<int:agendamento_id>/',
        views.comprovante,
        name='comprovante'
    ),

    path(
        'horarios-disponiveis/<int:servico_id>/',
        views.horarios_disponiveis,
        name='horarios_disponiveis'
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )