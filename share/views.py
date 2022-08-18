from __future__ import unicode_literals
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
import datetime
from .models import *
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from sharelink.settings import EMAIL_HOST_USER





def index(request):
	doc = Doc.objects.all()[0:1]
	return render(request, 'share/index.html', {'doc':doc})


def docs(request):
	if request.method == 'POST':
		doc_name = request.FILES.get('doc_name')

		Doc.objects.get_or_create(doc_name=doc_name)

		return HttpResponse('done')

	return render(request, 'share/docs.html')


def sendlink(request):
	if request.method == 'POST':

		try:
			send_mail('SHARED LINK', 
				""" Hello, a link has been shared with you from """ + EMAIL_HOST_USER +""".
				Below is the link to the resource.
				 """+ request.POST.get('url') +"""
				
				Click on this link to view.
				Thank You.""", 'test@gmail.com', [request.POST.get('email')])
		except Exception as e:
			errors = e.__str__()
			print("Email was not sent:", errors)
	return render(request, 'share/index.html')



def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():

			user = form.save()
			return redirect('home')

	else:
		form = SignUpForm()
	return render(request, 'share/signupform.html', {'form':form})



# ##################   Login view   ##########################################
def login_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =  request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponse('done')
		else:
			return HttpResponse('error')
					
	return render(request, 'share/login.html')




# ##################   Logout view   ##########################################
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/home')








""" mongo view """
def try_mongo_save(request):
	ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
	return HttpResponse('done')


def try_mongo_get(request):
	return HttpResponse(User.objects.all().filter(username="jed"))