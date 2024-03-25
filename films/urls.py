from django.urls import path
from . import views 

urlpatterns = [
    path('', views.FilmsListView.as_view(), name='index'),
    path('film_detial/<int:pk>/',views.FilmsDetailView.as_view(), name='film_detail'),
]