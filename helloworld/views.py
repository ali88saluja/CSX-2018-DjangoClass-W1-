from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse 
from django.contrib.auth.models import User
from ali88test.models import message


def index(request):
	return render(request, 'home.html', locals())

def home(request):
	return render(request, 'home.html', locals())

def ruden(request):
	return render(request, 'ruden.html', locals())

def sexy(request):
	return render(request, 'sexy.html', locals())

def InInDer(request):
	import random
	images_url= ['../static/img/chicken1.jpg' , '../static/img/chicken2.jpg' , '../static/img/chicken3.jpg' , '../static/img/chicken4.jpg' , '../static/img/chicken5.jpg' , '../static/img/chicken6.jpg' , '../static/img/chicken7.jpg' , '../static/img/chicken8.jpg' , '../static/img/chicken9.jpg' , '../static/img/chicken10.jpg' , '../static/img/chicken11.jpg' , '../static/img/chicken12.jpg','../static/img/chicken1.jpg' , '../static/img/chicken2.jpg' , '../static/img/chicken3.jpg' , '../static/img/chicken4.jpg' , '../static/img/chicken5.jpg' , '../static/img/chicken6.jpg' , '../static/img/chicken7.jpg' , '../static/img/chicken8.jpg' , '../static/img/chicken9.jpg' , '../static/img/chicken10.jpg' , '../static/img/chicken11.jpg' , '../static/img/chicken12.jpg']
	random.shuffle(images_url)
	return render(request, 'InInDer.html', locals())

def motto(request):
	return render(request, 'motto.html', locals())

def kilihime(request):
	import random
	imgs_url= ['../static/img/pic1.jpg' , '../static/img/pic2.jpg' , '../static/img/pic3.jpg' , '../static/img/pic4.jpg' , '../static/img/pic5.jpg' , '../static/img/pic6.jpg' , '../static/img/pic7.jpg' , '../static/img/pic8.jpg' , '../static/img/pic9.jpg' , '../static/img/pic10.jpg' , '../static/img/pic11.jpg' , '../static/img/pic12.jpg']
	random.shuffle(imgs_url)
	return render(request, 'kilihime.html', locals())
