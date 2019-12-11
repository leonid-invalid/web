from django.shortcuts import render
from accounts.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.db import IntegrityError

def SignUp(request):
	error = ''
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				user = form.save()
				login(request, user)
				url = '/'
				return HttpResponseRedirect(url)
			except IntegrityError:
				error = u'Duplicate username'
		else:
			error = u'Invalid input'
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {
		'form': form,
		'error': error,
	})
