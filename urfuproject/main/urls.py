from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('map', views.map, name='map'),
    path('skills', views.skills, name='skills'),
    path('job', views.job, name='job')
]