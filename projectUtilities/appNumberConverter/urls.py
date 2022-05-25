from django.urls import path
from appNumberConverter import views

app_name = 'appNumberConverter'
urlpatterns = [
    path('', views.numberConverter, name = 'numberConverter')
]
