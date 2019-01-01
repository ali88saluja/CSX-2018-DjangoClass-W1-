from django.shortcuts import render,redirect   
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		email = request.POST.get('email', False)

		try:
			user = User.objects.get(username=name)
		except:
			user = None
		if user is not None:
			message = '此使用者已經有人使用'
		else:
			user = User.objects.create_user(name, email, password)
			user.save()
			message = "註冊成功"
			return render(request, "index.html", locals())
	return render(request, 'register.html', locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None: 
			if user.is_active:
				auth.login(request,user)
				return redirect('/website.html/') 
				message = '登入成功!'
			else:
				message = '無此帳號!'
		else:
			message = '登入失敗!'
	return render(request,"login.html",locals()) 

def logout(request):
	auth.logout(request) 
	return redirect('/website.html/')