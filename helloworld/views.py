from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse 
from django.contrib.auth.models import User
from ali88test.models import message


def index(request):
	return render(request, 'home.html', locals())

def messages(request):
	import datetime
	if 'name' in request.POST:
		talker = request.POST.get('name',False)
		messages = request.POST.get('message',False)
		date_time = datetime.datetime.now()
		message.objects.create(send = talker , message = messages , time = date_time) 
		msgs = message.objects.all()
		return render(request, 'website.html', locals())
	else:
		msgs = message.objects.all()
		return render(request, 'website.html', locals())

