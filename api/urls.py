from django.contrib import admin
from django.urls import path
from .views import movie_list, review_list_create, register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('movies', movie_list),
    path('movies/<int:movie_id>/reviews/', review_list_create),
    path('register/', register),
    path('login/', obtain_auth_token)
]