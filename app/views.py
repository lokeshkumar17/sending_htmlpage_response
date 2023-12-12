from django.shortcuts import render

# Create your views here.
def vikings(request):
    return render(request,'me.html')
