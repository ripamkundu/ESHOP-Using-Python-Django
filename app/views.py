from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'index.html')
def AdminRegistration(request):
    return render(request, 'AdminRegistration.html')
def insertAdminDetails(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
        user.save()
        return render(request, 'index.html')
    else:
        return HttpResponse('<script> alert("Submission Error...!!!") </script>')
    

def userLogin(request):
    return render(request, 'login.html')
def userSignup(request):
    return render(request, 'signup.html')
