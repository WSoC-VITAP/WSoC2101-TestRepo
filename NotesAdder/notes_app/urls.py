from . import views
from django.urls import path
from .views import home_view, delete_view, add_view, add_note

app_name = 'notes_app'

urlpatterns = [
   # path('', views.IndexPage.as_view(), name='index'),
    path('', home_view),
    path('delete/<int:id>', delete_view),
    path('note_add/', add_view),
    path('add', add_note)

  #  path('frontend/', views.IndexPage.test(), name='frontend'),
    # path('backend/', views.BackEndPage.as_view(), name='backend')
]
