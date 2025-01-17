from django.shortcuts import render

# Create your views here.
def disp(request):
	return render(request, 'template/disp.html')