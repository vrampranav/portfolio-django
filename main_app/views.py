from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request,'main_app/index.html')
    return response
    

