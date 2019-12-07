
"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from qa.views import test, question_new, question_popular

urlpatterns = [
    path('', question_new, name='home'),
    path('login/', test, name='login'),
    path('signup/', test, name='signup'),
    path('question/', include('qa.urls'), name='question'),
    path('ask/', test, name='ask'),
    path('popular/', question_popular, name='popular'),
    path('new/', test, name='new'),
]
