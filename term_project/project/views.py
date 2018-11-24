from django.shortcuts import render

def summary(request):
	return render(request, 'project/summary.html')
	
def installations(request):
	return render(request, 'project/installations.html')

def tutorial(request):
	return render(request, 'project/tutorial.html')
	
def webpage(request):
	return render(request, 'project/webpage.html')
	
def report(request):
	return render(request, 'project/report.html')	
	
def credits(request):
	return render(request, 'project/credits.html')	