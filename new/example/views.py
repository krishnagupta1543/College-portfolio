from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#def home(request):
    #return HttpResponse("this is my page")
    #return render(request, 'home.html',{'name':'Ibrar'})
    #return render(request, 'service.html')
    #return render(request, 'login.html')
def register(request):
    form = UserCreationForm()
    return render(request, 'register.html',{'form': form})
