from django.urls import path
from views import PersonaList

urlpatterns = [
    path('Persona/', PersonaList.as_view(), name='persona_list')
]