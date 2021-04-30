from movie.views import home,register,movies,refresh,movie_details
from django.urls import path,include

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('movies/',movies,name='movies'),
    path('refresh/',refresh,name='refresh'),
    path('movies/<str:imdbID>/',movie_details,name='movie_details'),

]
