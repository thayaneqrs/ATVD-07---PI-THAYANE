from django.urls import path
from . import views

app_name = 'professores'

urlpatterns = [
    path('', views.lista_profs, name='professores_list'),
]