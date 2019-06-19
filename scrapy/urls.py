from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListPagesAndConteudo.as_view())
]