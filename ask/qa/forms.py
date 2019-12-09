from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		return self.cleaned_data 

	def save(self):
		self.cleaned_data['author'] = User.objects.get(pk=1)
		ask = Question.objects.create(**self.cleaned_data)
		ask.save()
		return ask

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.CharField(max_length=100)

	def clean(self):
		return self.cleaned_data 

	def save(self):
		self.cleaned_data['author'] = User.objects.get(pk=1)
		q = self.cleaned_data['question']
		self.cleaned_data['question'] = Question.objects.get(pk=int(q))
		answer = Answer.objects.create(**self.cleaned_data)
		answer.save()
		return answer
