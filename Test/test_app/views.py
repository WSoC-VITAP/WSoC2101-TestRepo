from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
app_name = 'test_app'


class IndexPage(TemplateView):
    template_name = 'test_app/index.html'


class FrontEndPage(TemplateView):
    template_name = 'test_app/frontend.html'


class BackEndPage(TemplateView):
    template_name = 'test_app/backend.html'
