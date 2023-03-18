from django.urls import path
from .views import EventoView,BoletoView
urlpatterns=[
    path('eventos/',EventoView.as_view(),name='eventos_list'),
    path('eventos/<int:id>',EventoView.as_view(),name='eventos_process'),
    path('boletos/',BoletoView.as_view(),name='boletos_list'),
    path('boletos/<int:id>',BoletoView.as_view(),name='boletos_process'),
    path('boletosEvento/<int:id>',BoletoView.get_boletos,name='boletosEvento_process'),
    path('searchEvento/',EventoView.get_eventos,name='searchEvento_process')
]