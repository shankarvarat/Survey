from django.shortcuts import render

# Create your views here.
def home(request):
    ma='ma'
    return render(request,'index.html')



