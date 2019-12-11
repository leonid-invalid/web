from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from qa.views import test, question_new, question_popular, ask

urlpatterns = [
    path('', question_new, name='home'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', include('accounts.urls')),
    path('question/', include('qa.urls')),
    path('ask/', ask, name='ask'),
    path('popular/', question_popular, name='popular'),
    path('new/', test, name='new'),
]
