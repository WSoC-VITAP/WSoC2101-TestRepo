from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'homepage'


class HomePage(TemplateView):
    template_name = 'homepage/profilepage.html'


class LoginPage(TemplateView):
    template_name = 'homepage/loginpage.html'
