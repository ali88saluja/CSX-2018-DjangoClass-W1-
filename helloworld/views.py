from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse 
from django.contrib.auth.models import User
from ali88test.models import message


def index(request):
	return render(request, 'home.html', locals())

def ruden(request):
	return render(request, 'ruden.html', locals())

def sexy(request):
	return render(request, 'sexy.html', locals())

def InInDer(request):
	return render(request, 'InInDer.html', locals())

def motto(request):
	return render(request, 'motto.html', locals())

def kilihime(request):
	return render(request, 'kilihime.html', locals())
