from django.urls import path
from appUnitConverter import views

app_name = 'appUnitConverter'
urlpatterns = [
    path('', views.unitConverter, name = 'unitConverter'),
    path('areaUnitConverter/', views.areaUnitConverter, name = 'areaUnitConverter'),
    path('dataUnitConverter/', views.dataUnitConverter, name = 'dataUnitConverter'),
    path('lengthUnitConverter/', views.lengthUnitConverter, name = 'lengthUnitConverter'),
    path('massUnitConverter/', views.massUnitConverter, name = 'massUnitConverter'),
    path('temperatureUnitConverter/', views.temperatureUnitConverter, name = 'temperatureUnitConverter'),
    path('volumeUnitConverter/', views.volumeUnitConverter, name = 'volumeUnitConverter')
]
