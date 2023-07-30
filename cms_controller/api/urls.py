from django.urls import path
from api.views import main

urlpatterns = [
    path('home', main),
]