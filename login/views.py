from django.shortcuts import render,redirect   
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
	
def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None: 
			if user.is_active:
				auth.login(request,user)
				return redirect('/website.html/') 
				
	return render(request,"login.html",locals()) 

def logout(request):
	auth.logout(request) 
	return redirect('/website.html/')