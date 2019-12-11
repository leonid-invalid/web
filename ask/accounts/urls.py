from accounts.views import SignUp
from django.urls import path

urlpatterns = (
	path('', SignUp, name='signup'),
)
