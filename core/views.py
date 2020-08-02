from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'registration/home.html')


def login(request):
    return render(request,'registration/login.html')


def signup(request):
    return render(request,'registration/signup.html')
