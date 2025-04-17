from django.contrib import admin
from django.urls import path
from .views import movie_list, review_list_create

urlpatterns = [
    path('movies', movie_list),
    path('movies/<int:movie_id>/reviews/', review_list_create),
]