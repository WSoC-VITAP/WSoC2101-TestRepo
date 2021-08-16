from . import views
from django.urls import path

app_name = 'homepage'

urlpatterns = [
    path('', views.HomePage.as_view(), name='profilepage')
]
