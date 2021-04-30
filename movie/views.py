from django.shortcuts import render,redirect
from movie.forms import UserRegisterForm
from movie.models import User,Movies,Genre
from django.contrib.auth.hashers import make_password
import os
from movie.src import search_movie
# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            context = {}
            context['directory']=directory = form.cleaned_data['Directory']
            context['name']=name = form.cleaned_data['Name']
            context['email']=email = form.cleaned_data['Email']
            context['username']=username = form.cleaned_data['Username']
            context['password']=password = make_password(form.cleaned_data['Password'])
            context['form'] = form
            user = User(name=name,email=email,password=password,basedir=directory,username=username)
            user.save()
            return render(request, 'register.html',context=context)
       
    form = UserRegisterForm()
    context = {'form':form}
    return render(request, 'register.html',context=context)

def movies(request):
    movie = Movies.objects.all()
    return render(request,'movies.html',context={'movie':movie})

def refresh(request):
    for file in os.listdir(request.user.basedir +'/Movies/'):
        movie  = search_movie.search(file)
        if movie != "":
            mov = Movies(title=movie['Title'],
                    year=movie['Year'],
                    genre=movie['Genre'],
                    actors=movie['Actors'],
                    poster = movie['Poster'],
                    plot=movie['Plot'],
                    imdbRating=float(movie['imdbRating']),
                    imdbID=movie['imdbID'],
                    types=movie['Type'],
                    user=request.user,
                    filename = file
            )
            mov.save()
            for gen in movie['Genre'].split(','):
                genre = Genre(genre=gen,title=mov)
                genre.save()

    return redirect('home')

def movie_details(request,imdbID):
    movie = Movies.objects.get(imdbID=imdbID)
    return render(request,'movie_details.html',context={'movie':movie})
