from django.urls import path
from . import views

urlpatterns = [
	path('', views.summary, name='summary'),
	path('installation/', views.installation, name='installation'),
	path('report/', views.report, name='report'),
	path('credits/', views.credits, name='credits'),
]