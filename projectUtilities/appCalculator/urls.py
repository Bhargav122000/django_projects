from django.urls import path
from appCalculator import views

app_name = 'appCalculator'
urlpatterns = [
    path('', views.calculator, name = 'calculator')
]
