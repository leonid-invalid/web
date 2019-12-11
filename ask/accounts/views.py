from django.shortcuts import render
from accounts.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

def SignUp(request):
	error = ''
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			form.save()
			url = '/'
			return HttpResponseRedirect(url)
		else:
			error = u'Invalid input'
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {
		'form': form,
	})
