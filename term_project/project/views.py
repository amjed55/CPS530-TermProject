from django.shortcuts import render

def summary(request):
	return render(request, 'project/summary.html')
	
def installation(request):
	return render(request, 'project/installation.html')
