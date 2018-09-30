from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	import random
	imgs_url= ['../static/img/pic1.jpg' , '../static/img/pic2.jpg' , '../static/img/pic3.jpg' , '../static/img/pic4.jpg' , '../static/img/pic5.jpg' , '../static/img/pic6.jpg' , '../static/img/pic7.jpg' , '../static/img/pic8.jpg' , '../static/img/pic9.jpg' , '../static/img/pic10.jpg' , '../static/img/pic11.jpg' , '../static/img/pic12.jpg']
	random.shuffle(imgs_url)
	return render(request, 'website.html', locals())