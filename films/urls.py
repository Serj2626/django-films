from django.urls import path
from . import views


urlpatterns = [
    path('', views.FilmsView.as_view(), name='home'),
    path('<slug:slug>/', views.FilmDetail.as_view()),
]