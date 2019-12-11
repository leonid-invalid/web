from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		return self.cleaned_data 

	def save(self, user):
		q = Question.objects.create(**self.cleaned_data, author=user)
		return q.id

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField()

	def clean(self):
		return self.cleaned_data 

	def save(self, user):
		q = self.cleaned_data['question']
		self.cleaned_data['question'] = Question.objects.get(pk=int(q))
		return Answer.objects.create(**self.cleaned_data, author=user)
