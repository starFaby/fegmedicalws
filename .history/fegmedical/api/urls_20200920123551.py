from django.urls import path
from views import PersonaList

urlspatterns = [
    path('Persona/', PersonaList.as_view(), name='persona_list')
]