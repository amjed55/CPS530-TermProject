from django.urls import path
from . import views

urlpatterns = [
	path('', views.summary, name='summary'),
	path('installations/', views.installations, name='installations'),
    # path('tutorial/', views.tutorial, name='tutorial'),	
    # path('webpage/', views.webpage, name='webpage'),	
	path('report/', views.report, name='report'),
	path('credits/', views.credits, name='credits'),
]