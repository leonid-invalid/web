from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from qa.models import Question, Answer
from django.core.paginator import Paginator
from qa.forms import AskForm, AnswerForm

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question_details(request, id):
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form.save()
			
			url = '/question/' + str(id) + '/'
			return HttpResponseRedirect(url)
	else:
		question = get_object_or_404(Question, id=id)
		answers=Answer.objects.filter(question=question)
		form = AnswerForm(initial={'question': question.id})
	return render(request, 'question_details.html', {
		'question': question,
		'answers': answers,
		'form': form,
})

@require_GET
def question_new(request):
	questions = Question.objects.new()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'question_new.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})

@require_GET
def question_popular(request):
	questions = Question.objects.popular()
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, 'question_popular.html', {
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
	})

def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			question = form.save()
			url = '/question/' + str(question.id) + '/'
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'AskAnswerForms.html', {'form': form})

#def answer(request):
#	if request.method == "POST":
#		form = AnswerForm(request.POST)
#		if form.is_valid():
#			answer = form.save()
#			url = answer.get_url()
#			return HttpResponseRedirect(url)
#	else:
#		form = AnswerForm()
#	return render(request, 'AskAnswerForms.html', {'form': form})
