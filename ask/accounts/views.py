from django.shortcuts import render
from accounts.forms import UserCreationForm
from django.http import HttpResponseRedirect

def SignUp(request):
	error = ''
	#question = get_object_or_404(Question, id=id)
	#answers = Answer.objects.filter(question=question)
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.clean()
			form.save()
			url = '/login/'
			return HttpResponseRedirect(url)
		else:
			error = u'Invalid input'
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {
		'form': form,
	})
