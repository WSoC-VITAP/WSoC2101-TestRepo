from . import views
from django.urls import path

app_name = 'homepage'

urlpatterns = [
    path('', views.HomePage.as_view(), name='profilepage'),
    path('login/', views.LoginPage.as_view(), name='loginpage'),
    path('carousel/', views.CarouselPage.as_view(), name='carouselpage')
]
