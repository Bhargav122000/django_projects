from django.urls import path
from appRomanConverter import views

app_name = 'appRomanConverter'
urlpatterns = [
    path('', views.romanConverter, name = 'romanConverter')
]
