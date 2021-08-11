from . import views
from django.urls import path

app_name = 'test_app'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index'),
    path('frontend/', views.FrontEndPage.as_view(), name='frontend'),
    path('backend/', views.BackEndPage.as_view(), name='backend')
]
