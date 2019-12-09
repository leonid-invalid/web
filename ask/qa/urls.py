from qa.views import test, question_details
from django.urls import path
urlpatterns = (
	path('<int:id>/', question_details, name='answer'),
	path('', test),	
)
