from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_home, name='news_home'),
    path('create/', views.create, name='create'),
]
