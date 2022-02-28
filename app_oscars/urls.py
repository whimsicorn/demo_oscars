from django.contrib import admin
from django.urls import path
from app_oscars.views import ranking_response

urlpatterns = [
   path('ranking/',ranking_response)
]
