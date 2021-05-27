from django.urls import path, include
from .views import HomeView


app_name = 'banks'
urlpatterns = [
    path('', HomeView, name = 'home'),
]