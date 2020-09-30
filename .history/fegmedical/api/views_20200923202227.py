from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.decorators.csrf import csrf_protect
from django.contrib.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

from .models import Persona
from .serializers import PersonaSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    succes_url = reverse_lazy('persona:persona_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

