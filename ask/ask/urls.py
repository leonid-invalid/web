from django.contrib import admin
from django.urls import path, include
from qa.views import test, question_new, question_popular, ask

urlpatterns = [
    path('', question_new, name='home'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/', include('qa.urls'), name='question'),
    path('ask/', ask, name='ask'),
    path('popular/', question_popular, name='popular'),
    path('new/', test, name='new'),
]
