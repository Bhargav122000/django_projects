from django.urls import path
from appWelcome import views

app_name = 'appWelcome'
urlpatterns = [
    path('', views.welcome, name = 'welcome'),
]
