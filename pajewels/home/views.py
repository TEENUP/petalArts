# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse


def index(request):
	return HttpResponse("hello")

def about_us(request):
	if isLoggedIn(request):
		# usr=User.objects.get(sponserId=sponserId)
		greet='<a class="page-scroll" href="/dashboard">Dashboard</a>'
		logout='<a class="page-scroll" href="/logout">Logout</a>'
		# Logout link
		return render(request, 'home/about_us.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet,'logout':logout})
	else:
		greet='<a class="page-scroll" href="/sign_up">Sign Up</a>'
		return render(request, 'home/about_us.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet})


def contact_us(request):
	if request.method == 'POST':
		subject= request.POST.get('subject')
		message= '%s %s' %(request.POST.get('message'),request.POST.get('name')+"("+request.POST.get('email')+")")
		emailFrom=request.POST.get('email')
		isEmailValid = validateEmail(emailFrom)
		errorEmail = ""
		if(not isEmailValid):
			errorEmail = "Please Enter A valid Email Id"

		emailTo= [settings.EMAIL_HOST_USER]
		send_mail(subject,message,emailFrom,emailTo,fail_silently=False)
		return redirect('/thanks')
		
	else:	
		if isLoggedIn(request):
			# usr=User.objects.get(sponserId=sponserId)
			greet='<a class="page-scroll" href="/dashboard">Dashboard</a>'
			logout='<a class="page-scroll" href="/logout">Logout</a>'
			# Can take email and name
			return render(request, 'home/contact_us.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet,'logout':logout,'errorEmail':errorEmail})
		else:
			greet='<a class="page-scroll" href="/sign_up">Sign Up</a>'
			return render(request, 'home/contact_us.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet,})


def thanks(request):
	if isLoggedIn(request):
		# usr=User.objects.get(sponserId=sponserId)
		greet='<a class="page-scroll" href="/dashboard">Dashboard</a>'
		logout='<a class="page-scroll" href="/logout">Logout</a>'
		# Logout link
		return render(request, 'home/thanks.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet,'logout':logout})
	else:
		greet='<a class="page-scroll" href="/sign_up">Sign Up</a>'
		return render(request, 'home/thanks.html', {'home':'/','about':'/about_us','products':'/products','contact':'/contact_us','greet':greet,'errorEmail':errorEmail})

def slide(request):
	return render(request, 'home/slide.html')
